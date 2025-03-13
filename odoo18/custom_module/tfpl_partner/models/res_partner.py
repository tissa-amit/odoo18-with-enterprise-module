# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    aadhar_number = fields.Char(string="Aadhar Number" )
    msme_registration = fields.Char(string="MSME Registration")
    tax_verified = fields.Boolean(string="Aadhar Pan Link", default=False)

    @api.constrains('tax_verified')
    def _check_aadhar_pan_link(self):
        for record in self:
            if not record.tax_verified:
                raise ValidationError("Your Aadhar Card and PAN Card are not linked. Please verify before proceeding.")
    vendor_group = fields.Selection([
        ('raw_materials', 'Raw Materials'),
        ('sub_contracting', 'Sub-Contracting Services'),
        ('room_rentals', 'Room Rentals'),
        ('machinery_hiring', 'Machinery Hiring'),
        ('expenses', 'Expenses'),
        ('logistics', 'Logistics'),
        ('testing_certification', 'Testing Certification'),
    ], string="Vendor Group")
    supplier_type = fields.Selection([
        ('supply', 'Supply'),
        ('service', 'Service'),
    ], string="Supplier Type")
    service_type = fields.Selection([
        ('machinery_hires', 'Machinery Hires'),
    ], string="Service Type")
    supplier_address = fields.Text(string="Supplier Address")
    nick_name = fields.Char(string="Nick Name")
    l10n_in_pan = fields.Char(string="Pan")
    # state = fields.Char(string="State", required=True)
