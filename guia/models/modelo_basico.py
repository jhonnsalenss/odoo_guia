# -*- coding: utf-8 -*-

from odoo import fields, models

class ModeloBasico(models.Model):
     _name = 'modelo.basico'
     _description = 'Ejemplo de modelo basico'

     name = fields.Char(required=True)
     description = fields.Text()
     postcode = fields.Char()
     date_availability = fields.Datetime()
     expected_price = fields.Float(required=True)
     selling_price = fields.Float(readonly=True)
     bedrooms = fields.Integer()
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
     
