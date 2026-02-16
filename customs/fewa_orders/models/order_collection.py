from odoo import models,fields,api,_

class FewaOrderCollection(models.Model):
    _name="fewa.order.collection"
    _description="Fewa Order Collection"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Ref No.")
    order_date = fields.Date(string="Order Date", default = fields.Date.today())
    company_id = fields.Many2one('res.company',string="Company")
    group_name = fields.Char(string="Group Name",related='company_id.group_name',store=True)
    order_line = fields.One2many('fewa.user.orders','collection_id',string="Order Line") 
    order_from = fields.Many2one("res.company",string="Caterer",related='company_id.caterer_id')
    state = fields.Selection([('draft','Draft'),('done','Done')],string="State",default='draft')

    
    @api.model
    def create(self,vals):
        if not vals.get('name', False):
            vals['name'] = self.env['ir.sequence'].next_by_code('fewa.order.collection') or '/'
        return super(FewaOrderCollection, self).create(vals)

    
    