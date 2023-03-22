
from odoo import fields, models, api

class ModeloVenta(models.Model):
    _name = 'modelo.venta'
    _description = 'Ejemplo de modelo venta'

    id_cliente = fields.Many2one('modelo.cliente', string="cliente")
    name = fields.Char()
    description = fields.Text()
    date = fields.Datetime(copy=False)
    price = fields.Float(required=True)
    reference = fields.Char(string="Reference")

    @api.onchange('id_cliente')
    def onchange_id_cliente(self):
        self.reference = self.id_cliente.reference

    def action_test(self):
        print("Button clicked !!!")