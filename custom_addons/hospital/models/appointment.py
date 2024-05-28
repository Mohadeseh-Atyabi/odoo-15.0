from odoo import api, fields, models, _, tools


class HospitalAppointment(models.Model):
    # It creates a table named hospital_patient
    _name = "hospital.appointment"
    # Inherit these models to use in chatter
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    # To add any to one field, we should name it as 'model_id'.
    patient_id = fields.Many2one(comodel_name='hospital.patient', string='Patient')
    # Creates a read only field from the Patient model. By adding 'readonly=False', we can make this field editable.
    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string="Reference")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
