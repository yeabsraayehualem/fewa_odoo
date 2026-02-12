from odoo import models,fields,api,_
from datetime import timedelta

class FewaUsersMealPlan(models.Model):
    _name="fewa.user.meal.plan"


    name = fields.Many2one('fewa.meal.plan',string="Meal Plan")
    user_id = fields.Many2one('res.users',string="Customer")
    activated_date=fields.Date(string="Activated Date",default=fields.Date.today())
    expiration_date = fields.Date(string='Expiration Date',default=fields.Date.today() + timedelta(days=30))
    plan_available_orders = fields.Integer(related='name.available_orders')
    ordered = fields.Integer(string="Ordered", compute="_total_orderd",store=True)
    remaining = fields.Integer(string="Remaining",compute="_total_remaining" ,store=True)
    orders = fields.One2many("fewa.user.orders","plan_id")
    status = fields.Selection(
        [(i,i.capitalize()) for i in ['draft','active','expired']]
    )
    company_id = fields.Many2one('res.company', related='user_id.company_id')
    image = fields.Binary(string="Image",related='user_id.image_1920')

    @api.depends("orders")
    def _total_remaining(self):
        for rec in self:
            rec.remaining = rec.plan_available_orders - len(rec.orders)


    @api.depends("orders")
    def _total_orderd(self):
        for rec in self:
            rec.ordered = len(rec.orders)
    
    def action_activate(self):
        self.status = 'activated'
        self.action_activate = fields.Date.today()


    @api.model 
    def cron_expire(self):
        expired_plans = self.env['fewa.user.meal.plan'].search([('status','=','active'),('expiration_date','<=',fields.Date.today())])
        for explan in expired_plans:
            explan.status = 'expired'
            explan.expiration_date = fields.Date.today()




class FewaUserOrders(models.Model):
    _name="fewa.user.orders"
    _order = "id desc"


    name = fields.Char(string="Ref No.")
    plan_id = fields.Many2one('fewa.user.meal.plan',stiring="Order Package")
    meal_id = fields.Many2one('fewa.meals',string="Meal")
    ordered_date = fields.Date(string="Ordered Date", default = fields.Date.today())
    order_from = fields.Many2one("res.company",string="Caterer",domain=[('business_type','=','caterer')])
    assigned_driver = fields.Many2one('res.users',string="Assigned User")
    status = fields.Selection([(i,i.capitalize()) for i in ['draft','accepted','ready','ondelivery','delivered']],string="Status", default="draft" )
    meal_image = fields.Binary(related="meal_id.image")
    company_id = fields.Many2one('res.company',string="Company")

    def action_accept_order(self):
        for rec in self:
            rec.status = 'accepted'


    def action_ready_order(self):
        for rec in self:
            rec.status = 'ready'


    def action_ondelivery_order(self):
        for rec in self:
            rec.status = 'ondelivery'


    def action_delivered_order(self):
        for rec in self:
            rec.status = 'delivered'

