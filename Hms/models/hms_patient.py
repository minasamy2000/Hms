from odoo import fields, models,api
import re
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta
class Patient(models.Model):
    _name = 'patient'
    # _inherits = ['mail.thread', 'mail.activity.mixin']
    _description = 'patient'
    _rec_name='firstname'

    firstname= fields.Char('First name:', required=True)
    lastname= fields.Char('Last name',required=True)
    Birthday= fields.Datetime('Birthday')
    history=fields.Html('History')
    cr_ratio=fields.Float('cr ratio')
    blood= fields.Selection([
        ('b', 'B'),
        ('a', 'A'),
        ('b+', 'B+'),
    ], string='Blood')
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string='state',default='undetermined')
    pcr= fields.Boolean(string='PCR')
    image=fields.Binary('image')
    email=fields.Text('Email')
    address=fields.Text('Address')
    age=fields.Char("Age",compute='_compute_age')
    department_id = fields.Many2many("department", string="Department",)
    doctor_id = fields.Many2many("doctor", string="Doctor" ,groups='Hms.hms_manager')
    history_id=fields.One2many("hms.patient.history","patient_id")

    def _compute_age(self):
        for rec in self:
            if rec.Birthday:
               rec.age = relativedelta(fields.Date.today(), rec.Birthday).years
            else:
                rec.age=0
    def good(self):
        self.state="good"
    def fair(self):
        self.state="fair"
    def serious(self):
        self.state = "serious"

    @api.constrains('email')
    def check_value_constraint(self):
        for rec in self:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", rec.email):
               raise UserError("invalid Email")







