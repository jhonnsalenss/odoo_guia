from odoo import models, fields

class EspecialidadHospital(models.Model):
    _name = 'especialidad.hospital'
    _description = 'Especialidad del doctor'

    nombre = fields.Char(string="Codigo de especialidad", required=True)
    nombre_especialidad = fields.Char(string="Nombre de la especialidad", required=True)
#    id_doctor = fields.Many2many('doctor.hospital',string="Codigo del doctor",required=True)
    