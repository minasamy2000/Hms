from odoo import models,fields
class Patient(models.Model):
    _name = 'doctor'
    _description = 'doctor'
    _rec_name = 'firstname'

    firstname= fields.Char('First name:', required=True)
    lastname= fields.Char('Last name',required=True)
    image= fields.Binary('Image')
    patient_id = fields.Many2many("patient", string="Patient")
    # history_id = fields.One2many("hms.doctor.history", "doctor_id")