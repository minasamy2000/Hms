from odoo import fields, models
class Deparment(models.Model):
    _name = 'department'
    _description = 'department'
    _rec_name = 'name'

    name= fields.Char('name:', required=True)
    capacity= fields.Integer('Capacity')
    is_opend= fields.Boolean('Is_Opened')
    doctor_id = fields.Many2many("doctor",string="Doctor")