from odoo import models,fields,api,_
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = 'res.company'
    


    business_type = fields.Selection([
        ('caterer', 'Caterer'),
        ('customer', 'Customer'),
        ('delivery', 'Delivery'),
        ('main', 'Main'),
    ], string='Business Type', default='main')

    caterer_id = fields.Many2one('res.company',domain = [('business_type','=','caterer')])
    cusotmers= fields.One2many('res.company','caterer_id')
    delivery_id = fields.Many2one('res.company',domain = [('business_type','=','delivery')])

    @api.onchange('business_type')
    def onchange_business_type(self):
        if self.business_type == 'main':
            res = self.env["res.company"].search_count([('business_type', '=', 'main')])
            if res > 1:
                raise ValidationError(_("Only one company can be main"))


    
    def action_activate(self):
        self.active = True
    

    def action_deactivate(self):
        self.active = False

    

    def action_activate_multiple(self):
        for rec in self:
            rec.active = True

    def action_deactivate_multiple(self):
        for rec in self:
            rec.active = False