# -*- coding: utf-8 -*-

from odoo import fields, models

class basic(models.Model):
     _name = 'basic.model'
     _description = 'Basic model test'

     name = fields.Char(required=True)
     description = fields.Text()
     postcode = fields.Char()
     date_availability = fields.Datetime()
     expected_price = fields.Float(required=True)
     selling_price = fields.Float()
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
     
