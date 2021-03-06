# -*- coding:Utf-8 -*-

from tastypie import fields as base_fields
from tastypie_mongoengine import fields

from core.api.utils import (
    TenantResource,
    ZombieMixinResource,
    WakeUpMixinResource
)
from core.models import VosaeUser
from core.api.doc import HELP_TEXT
from core.tasks import fill_user_initial_data


__all__ = (
    'VosaeUserResource',
)


class VosaeUserResource(WakeUpMixinResource, ZombieMixinResource, TenantResource):
    full_name = base_fields.CharField(
        attribute='get_full_name',
        readonly=True,
        help_text=HELP_TEXT['vosae_user']['full_name']
    )
    email = base_fields.CharField(
        attribute='email',
        help_text=HELP_TEXT['vosae_user']['email']
    )
    status = base_fields.CharField(
        attribute='status',
        blank=True,
        help_text=HELP_TEXT['vosae_user']['status']
    )
    photo_uri = base_fields.CharField(
        attribute='photo_uri',
        readonly=True,
        null=True,
        blank=True,
        help_text=HELP_TEXT['vosae_user']['photo_uri']
    )
    specific_permissions = base_fields.DictField(
        attribute='specific_permissions',
        blank=True,
        help_text=HELP_TEXT['vosae_user']['specific_permissions']
    )
    permissions = base_fields.ListField(
        readonly=True,
        help_text=HELP_TEXT['vosae_user']['permissions']
    )

    groups = fields.ReferencedListField(
        of='core.api.resources.VosaeGroupResource',
        attribute='groups',
        null=True,
        blank=True,
        help_text=HELP_TEXT['vosae_user']['groups']
    )
    settings = fields.EmbeddedDocumentField(
        embedded='core.api.resources.VosaeUserSettingsResource',
        attribute='settings',
        help_text=HELP_TEXT['vosae_user']['settings']
    )

    class Meta(TenantResource.Meta):
        resource_name = 'user'
        queryset = VosaeUser.objects.all()
        list_allowed_methods = ('get', 'post')
        excludes = ('tenant',)
        filtering = {
            "email": ('exact',)
        }

    def obj_create(self, bundle, **kwargs):
        """Fills initial data (based on request's language) after VosaeUser creation"""
        bundle = super(VosaeUserResource, self).obj_create(bundle, **kwargs)

        # Fill user initial data (Tenant and VosaeUser are required)
        fill_user_initial_data.delay(bundle.obj, bundle.request.LANGUAGE_CODE)

        return bundle

    def hydrate_email(self, bundle):
        """
        Email can only be used on POST (creation) in order to link the
        :class:`~core.models.VosaeUser` to the Django user.
        """
        if bundle.request.method.lower() != 'post':
            bundle.data.update(email=bundle.obj.email)
        return bundle

    def dehydrate_permissions(self, bundle):
        """Returns the list of acquired permissions"""
        return list(bundle.obj.permissions.acquired)
