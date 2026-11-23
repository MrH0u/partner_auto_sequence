from odoo import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):

        if vals.get('ref'):
            return super().create(vals)

        if vals.get('supplier_rank'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'supplier.sequence'
            )
        elif vals.get('customer_rank'):
            vals['ref'] = self.env['ir.sequence'].next_by_code(
                'partner.sequence'
            )

        return super().create(vals)