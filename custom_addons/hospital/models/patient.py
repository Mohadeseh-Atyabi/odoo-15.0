from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    # It creates a table named hospital_patient
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Name')
    age = fields.Integer(string="age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
