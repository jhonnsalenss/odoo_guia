from odoo import models, fields

class CitaHospital(models.Model):
    _name = 'cita.hospital'
    _description = 'Citas en el hospital'

#    name = fields.Char(string = "Codigo de la cita", required = True)
#    id_doctor_cita = fields.Many2one('doctor.hospital', string = "Codigo del doctor",required=True)
#    id_sala_cita = fields.Many2one('sala.hospital', string="Numero de la sala",required=True)
#    id_paciente_cita = fields.Many2one('paciente.hospital',string="DNI del paciente",required=True)
#    fecha_cita = fields.Date(string="Fecha de la cita",required=True)
#    especialidad = fields.Text(string="Especialidad")
