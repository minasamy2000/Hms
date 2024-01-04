from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    phone = fields.Char('Phone', required=True)
    data=fields.Char('data')

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("inside action_confirm method")
        return res
