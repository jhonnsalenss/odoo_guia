from odoo import models, fields

class DoctorHospital(models.Model):
    _name = 'doctor.hospital'
    _description = 'Datos de doctor hospital'

    name = fields.Char(string="Codigo del doctor",required=True)
    id_especialidad_doctor = fields.Many2many('especialidad.hospital',string="Codigo de la especialidad",required=True)
    foto = fields.Binary()
    nombre_doctor = fields.Text(string="Nombre del doctor",required=True)
    apellido_doctor = fields.Text(string="Apellido del doctor",required=True)
    celular_doctor = fields.Char(string="Celular del doctor",size=9)
    n_colegiatura = fields.Char(string="Numero de colegiatura")
    id_cita_doctor = fields.One2many('cita.hospital','id_doctor_cita',string="Citas del doctor")