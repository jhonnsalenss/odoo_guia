
from odoo import fields, models

class ModeloTienda(models.Model):
    _name = 'modelo.tienda'
    _description = 'Ejemplo de modelo tienda'

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Datetime(copy=False)
    expected_price = fields.Float(required=True)