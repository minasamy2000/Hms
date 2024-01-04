from odoo import fields, models, api


class Contacts(models.Model):
    _inherit = 'res.partner'

    phone = fields.Char('Phone', required=True)
    data=fields.Char('data')
    def action_confirm(self):
        res = super(Contacts, self).action_confirm()
        print("inside action_confirm method")
        return res