from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    enquiry_type = fields.Selection([
        ('mechanical_piping', 'Mechanical Piping'),
        ('fire_protection', 'Fire Protection Systems'),
        ('equipment_fabrication', 'Equipment Fabrication'),
        ('structural_work', 'Structural Work'),
        ('electrical', 'Electrical Work'),
        ('instrumentation', 'Instrumentation'),
        ('insulation', 'Insulation')
    ], string="Enquiry Type")

    enquiry_source = fields.Selection([
        ('ceo_contacts', 'CEO Contacts'),
        ('head_office', 'Head Office'),
        ('branch_office', 'Branch Office'),
        ('consultants', 'Consultants (Tata, JLL)'),
        ('other', 'Other')
    ], string="Enquiry Source")

    enquiry_stage = fields.Selection([
        ('new', 'New'),
        ('analysis', 'Under Analysis'),
        ('proposal_sent', 'Proposal Sent'),
        ('negotiation', 'Negotiation'),
        ('approved', 'Approved'),
        ('lost', 'Lost')
    ], string="Enquiry Stage", default='new')


    approved = fields.Boolean(string="Approved", default=False)

    def action_approve_lead(self):
        """Move the lead to the 'Done' stage when approved"""
        done_stage = self.env['crm.stage'].search([('name', '=', 'Done')], limit=1)
        if done_stage:
            self.write({'stage_id': done_stage.id})
