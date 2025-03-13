from odoo import models, fields

class FirstModel(models.Model):
    _name = 'first.model'
    _description = 'First Model'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
