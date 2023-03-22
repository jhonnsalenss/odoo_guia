from datetime import date
from odoo import fields, models, api

class ModeloCliente(models.Model):
    _name = 'modelo.cliente'
    _description = 'cliente de tienda'

    name = fields.Char()
    number = fields.Integer(default=1)
    reference = fields.Char(string="Reference")
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age')
    
    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 2

