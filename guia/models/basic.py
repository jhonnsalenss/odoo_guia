# -*- coding: utf-8 -*-

from odoo import fields, models

class basic(models.Model):
     _name = 'basic.basic'
     _description = 'Basic model test'

     name = fields.Char()