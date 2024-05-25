from odoo import api, fields, models, _, tools
from datetime import date


class HospitalPatient(models.Model):
    # It creates a table named hospital_patient
    _name = "hospital.patient"
    # Inherit these models to use in chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    # We cannot use a non-stored computed field in the search view
    age = fields.Integer(string="Age", compute='_compute_age')
    ref = fields.Char(string='Reference')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    # By adding this field, we enable the model to be archived/unarchived by setting this field equal to True/False
    active = fields.Boolean(string="Active", default=True)

    # Any changes in the date_of_birth field leads to executing this function
    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0
