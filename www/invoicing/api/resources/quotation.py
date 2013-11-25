# -*- coding:Utf-8 -*-

from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist

from tastypie import fields as base_fields, http
from tastypie.utils import trailing_slash
from tastypie_mongoengine import fields

from invoicing.models import Quotation
from invoicing.api.resources.invoice_base import InvoiceBaseResource
from invoicing.api.resources.mixins import InvoiceMakableResourceMixin
from invoicing.api.doc import HELP_TEXT


__all__ = (
    'QuotationResource',
)


class QuotationResource(InvoiceBaseResource, InvoiceMakableResourceMixin):
    state = base_fields.CharField(
        attribute='state',
        readonly=True,
        help_text=HELP_TEXT['quotation']['state']
    )

    current_revision = fields.EmbeddedDocumentField(
        embedded='invoicing.api.resources.QuotationRevisionResource',
        attribute='current_revision',
        help_text=HELP_TEXT['quotation']['current_revision']
    )
    revisions = fields.EmbeddedListField(
        of='invoicing.api.resources.QuotationRevisionResource',
        attribute='revisions',
        readonly=True,
        null=True,
        blank=True,
        help_text=HELP_TEXT['quotation']['revisions']
    )

    class Meta(InvoiceBaseResource.Meta):
        queryset = Quotation.objects.all()
        detail_specific_methods = ('make_purchase_order', 'make_down_payment_invoice', 'make_invoice', 'mark_as_awaiting_approval')

    def prepend_urls(self):
        """Add urls for resources actions."""
        urls = super(QuotationResource, self).prepend_urls()
        urls.extend((
            url(r'^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/make_purchase_order%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('make_purchase_order'), name='api_quotation_make_purchase_order'),
            url(r'^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/make_down_payment_invoice%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('make_down_payment_invoice'), name='api_quotation_make_down_payment_invoice'),
            url(r'^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/make_invoice%s$' % (self._meta.resource_name, trailing_slash()), self.wrap_view('make_invoice'), name='api_quotation_make_invoice'),
        ))
        return urls

    def make_purchase_order(self, request, **kwargs):
        """Create a purchase order from a quotation"""
        from invoicing.api.resources.purchase_order import PurchaseOrderResource
        self.method_check(request, allowed=['put'])
        self.is_authenticated(request)
        self.throttle_check(request)

        try:
            bundle = self.build_bundle(request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return http.HttpNotFound()

        purchase_order = obj.make_purchase_order(request.vosae_user)
        purchase_order_resource = PurchaseOrderResource()
        purchase_order_resource_bundle = purchase_order_resource.build_bundle(obj=purchase_order, request=request)

        self.log_throttled_access(request)

        to_be_serialized = {
            'purchase_order_uri': purchase_order_resource.get_resource_uri(purchase_order_resource_bundle)
        }
        to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
        return self.create_response(request, to_be_serialized)
