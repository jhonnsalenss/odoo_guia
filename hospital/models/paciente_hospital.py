from odoo import models, fields

class PacienteHospital(models.Model):
    _name = 'paciente.hospital'
    _description = 'Ficha de paciente'

    dni = fields.Char(string="DNI del paciente",required=True,size=8)
    nombre = fields.Char(string="Nombre del paciente", required=True)
    apellido = fields.Char(string="Apellido del paciente", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    celular = fields.Char(string="Celular",size=9)
    id_cita_paciente = fields.One2many('cita.hospital','id_paciente_cita', string="citas del paciente")
    id_registroclinico = fields.One2many('registroclinico.hospital','id_paciente_registro',string="Registro clinico del paciente")
    

    