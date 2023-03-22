# -*- coding: utf-8 -*-

from odoo import fields, models

class ModeloBasico(models.Model):
     _name = 'modelo.basico'
     _description = 'Ejemplo de modelo basico'

     name = fields.Char(required=True, default="Unknown")
     description = fields.Text()
'''
     postcode = fields.Char()
     date_availability = fields.Datetime(copy=False)
     expected_price = fields.Float(required=True)
     selling_price = fields.Float(readonly=True,copy=False)
     bedrooms = fields.Integer(default="2")
     living_area = fields.Integer()
     facades = fields.Integer()
     garage = fields.Boolean()
     garden = fields.Boolean()
     garden_area = fields.Integer()
     garden_orientation = fields.Selection([
          ('North','LabelNorth'),
          ('South','LabelSouth'),
          ('East','LabelEast'),
          ('West','LabelWest')
          ])
     last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())

'''