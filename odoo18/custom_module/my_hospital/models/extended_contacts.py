from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_handicap = fields.Boolean(string="Is Handicap")
    is_partner = fields.Boolean(string="Is Partner")

    stage = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
    ], string="Stage", default="draft")


    def extended_contacts_dummy_button(self):
        """Move to the next stage when button is clicked"""
        stage_order = ['draft', 'confirmed', 'done']
        current_stage_index = stage_order.index(self.stage)
        if current_stage_index < len(stage_order) - 1:
            self.stage = stage_order[current_stage_index + 1]




