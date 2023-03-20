from odoo import models, fields

class RegistroclinicoHospital(models.Model):
    _name = 'registroclinico.hospital'
    _description = 'Registro clinico del hospital'

    nombre = fields.Char(string = "Codigo del registro", required=True)
    id_paciente_registro = fields.Many2one('paciente.hospital',string="DNI del paciente")
    diagnostico = fields.Text(string="diagnostico del paciente")
    receta = fields.Text(string="Receta del paciente")
    examen = fields.Text(string="Examen del paciente")