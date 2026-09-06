from odoo import models, fields

class PosOrder(models.Model):
    _inherit = 'pos.order'

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        required=True,
        default=lambda self: self.env.company
    )
