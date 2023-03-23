# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Herencia de modelo Sale order'

    confirmed_user_id = fields.Many2one('res.users', string="Uso de herencia usuario confirmado")