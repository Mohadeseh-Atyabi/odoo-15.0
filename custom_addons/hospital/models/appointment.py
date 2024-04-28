from odoo import api, fields, models, _, tools


class HospitalAppointment(models.Model):
    # It creates a table named hospital_patient
    _name = "hospital.appointment"
    # Inherit these models to use in chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"

    # To add any to one field, we should name it as 'model_id'.
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
