# -*- coding:Utf-8 -*-

HELP_TEXT = {
    'invoicebase': {
        'reference': 'Reference of the quotation/invoice/credit note',
        'total': 'Total amount',
        'amount': 'Total amount minus down-payment invoices amounts (ie. expected amount to pay)',
        'account_type': 'Account type.\nOne of: <ul><li class="text-info">PAYABLE</li> <li class="text-info">RECEIVABLE</li></ul>',
        'issuer': 'User in charge of the quotation/invoice/credit note',
        'organization': 'Billed organization',
        'contact': 'Billed contact',
        'current_revision': 'The current quotation/invoice/credit note revision',
        'revisions': 'All past quotation/invoice/credit note revisions',
        'history': 'All history actions',
        'notes': 'Notes related to the quotation/invoice/credit note',
        'attachments': 'Attachments related to the quotation/invoice/credit note',
    },
    'quotation': {
        'state': 'Quotation state.\nOne of: <ul><li class="text-info">DRAFT</li> <li class="text-info">AWAITING_APPROVAL</li> <li class="text-info">APPROVED</li> <li class="text-info">REFUSED</li> <li class="text-info">EXPIRED</li> <li class="text-info">INVOICED</li></ul>',
        'related_invoice': 'The invoice related to the quotation',
        'related_invoices_cancelled': 'All related invoices that have been cancelled',
        'down_payments': 'All down-payment invoices related to the quotation',
    },
    'invoice': {
        'state': 'Invoice state.\nOne of: <ul><li class="text-info">DRAFT</li> <li class="text-info">REGISTERED</li> <li class="text-info">OVERDUE</li> <li class="text-info">PART_PAID</li> <li class="text-info">PAID</li> <li class="text-info">CANCELLED</li></ul>',
        'paid': 'Invoice\'s paid amount',
        'balance': 'Invoice\'s balance amount',
        'has_temporary_reference': 'Invoices and down-payment invoices references must follow a continuous numbering scheme. So, only charged invoices have a well-defined reference. This indicates if the invoice has a temporary reference',
        'related_quotation': 'Invoice\'s related quotation',
        'related_credit_note': 'Invoice\'s related credit note',
        'payments': 'Invoice\'s related payments',
    },
    'downpayment': {
        'state': 'Down-payment invoice state.\nOne of: <ul><li class="text-info">DRAFT</li> <li class="text-info">REGISTERED</li> <li class="text-info">OVERDUE</li> <li class="text-info">PART_PAID</li> <li class="text-info">PAID</li> <li class="text-info">CANCELLED</li></ul>',
        'percentage': 'Down-payment invoice percentage applied on the quotation total amount',
        'tax_applied': 'Tax applied on the down-payment invoice amount',
    },
    'creditnote': {
        'state': 'Credit note state.\nOne of: <ul><li class="text-info">REGISTERED</li> <li class="text-info">SENT</li> <li class="text-info">PAID</li></ul>',
        'related_invoice': 'Credit note\'s related invoice',
    },
    'item': {
        'reference': 'Reference of the item.\nThis is internal and won\'t be displayed on a generated document.\nLimited to this set of chars: [a-zA-Z0-9_-] (max_length = 32)',
        'description': 'Item\'s description (multiline, max_length = 512)',
        'unit_price': 'Item\'s unit price (excluding taxes)',
        'type': 'Item\'s type',
        'currency': 'Item\'s currency. Works with the acquired price.\nUsed to process a currency conversion based on current exchange rates',
        'tax': 'Item\'s tax',
    },
    'currency': {
        'symbol': 'Currency\'s ISO 4217 symbol',
        'rates': 'Currency\'s rates',
    },
    'tax': {
        'name': 'Tax name (max_length = 64)',
        'rate': 'Tax rate',
    },
    'payment': {
        'issued_at': 'Payment\'s creation datetime on Vosae',
        'date': 'Payment\'s reception date',
        'amount': 'Payment\'s amount',
        'type': 'Payment\'s type.\nOne of: <ul><li class="text-info">CASH</li> <li class="text-info">CHECK</li> <li class="text-info">CREDIT_CARD</li> <li class="text-info">TRANSFER</li> <li class="text-info">OTHER</li></ul>',
        'note': 'Payment\'s note',
        'issuer': 'The used which have registered the payment on Vosae',
        'currency': 'Payment\'s currency',
        'invoice': 'The related invoice',
        'down_payment_invoice': 'The related down-payment invoice',
    },
    'invoice_revision': {
        'revision': 'UID of the revision',
        'issue_date': 'Revision\'s creation datetime',
        'sender': 'Name of the sender (person)',
        'sender_organization': 'Sender\'s organization',
        'quotation_date': 'Quotation issue date',
        'quotation_validity': 'Quotation validity date.\nFree value, must be greater than or equal to <code>quotation_date</code>',
        'invoicing_date': 'Invoice issue date',
        'due_date': 'Invoice due date.\nFree value, must be greater than or equal to <code>invoicing_date</code>.\n<span class="label label-warning">Warning</span> A maximum duration may exist depending on your registration country',
        'credit_note_emission_date': 'Emission date of the credit note',
        'custom_payment_conditions': 'Custom payment conditions.\nIn some businesses custom payment conditions may be applied depending on the work or the delivery process.\nIn such cases, <code>due_date</code> acts as an expected due date used for budget projections',
        'customer_reference': 'Some customers may request to figure a reference on the generated documents, linked to their tools.\nThis <code>customer_reference</code> is displayed between the document reference and the line items',
        'taxes_application': 'Taxes application.\nOne of: <ul><li class="text-info">EXCLUSIVE</li> <li class="text-info">NOT_APPLICABLE</li></ul>',
        'issuer': 'The Vosae user which has created this revision',
        'sender_address': 'Address of the sender',
        'contact': 'The contact linked to this revision',
        'organization': 'The organization linked to this revision',
        'billing_address': 'The billing address',
        'delivery_address': 'The delivery address',
        'currency': 'The currency used.\nThis is an embedded snapshot on which are based items conversions (if needed)',
        'line_items': 'The items present in the revision',
        'pdf': 'A language-based dictionnary of previously generated PDFs of the document revision',
    },
    'invoice_note': {
        'datetime': 'Note\'s creation datetime',
        'note': 'Note\'s content',
        'issuer': 'User which have created the note',
    },
    'invoice_item': {
        'reference': 'Invoice item\'s reference, related to the item',
        'description': 'Invoice item\'s description, can override the original item\'s description',
        'quantity': 'Invoice item\'s quantity',
        'unit_price': 'Invoice item\'s unit price',
        'tax': 'Invoice item\'s tax',
    },
    'exchange_rate': {
        'currency_to': 'Exchange rate\'s target currency',
        'datetime': 'Acquisition datetime of the exchange rate',
        'rate': 'Exchange rate\'s actual rate',
    },
    'history_entry': {
        'datetime': 'History entry\'s datetime',
        'issuer': 'User which have done an action resulting in the history entry\'s creation',
        'revision': 'Revision related to the history entry',
        'action': 'History entry\'s action',
        'state': 'New state of the quotation/invoice/credit note',
        'sent_method': 'Sent method of the history entry.\nOne of: <ul><li class="text-info">EMAIL</li></ul>',
        'sent_to': 'Receiver of the sent method (max_length = 128)',
    },
}
