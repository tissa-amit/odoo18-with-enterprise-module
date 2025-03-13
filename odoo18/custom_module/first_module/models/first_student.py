from odoo import models, fields

class Firststudent(models.Model):
    _name = 'first.student'
    _description = 'First Model'

    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
