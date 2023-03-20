from odoo import models, fields

class SalaHospital(models.Model):
    _name = 'sala.hospital'
    _description = 'Sala del Hospital'

    nombre = fields.Char(string="Numero de sala del hospital", required=True)
    ubicacion = fields.Char(string="Ubicacion de la sala")
    id_cita_sala = fields.One2many('cita.hospital','id_sala_cita',string="Citas de la sala")