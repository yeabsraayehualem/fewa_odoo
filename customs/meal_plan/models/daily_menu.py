from odoo import models, fields, api, _

class MealMenu(models.Model):
    _name = "meal.menu"
    _description = "Meal Menu"

    name = fields.Char(string="Menu", default="New")
    date = fields.Date(string="Date", default=fields.Date.today)
    meal_plans = fields.Many2many("fewa.meal.plan", string="Meal Plans")
    meals_menu = fields.One2many('active.meals', 'meal_menu', string="Meals Menu", compute="_populate_meal_menu", store=True)
    active_meals = fields.Integer(string="Active",compute="_compute_active_meals")
    inactive_meals = fields.Integer(string="Active",compute="_compute_inactive_meals")
    company_id = fields.Many2one('res.company',string="Company",default=lambda self: self.env.company.id)
    active = fields.Boolean(string="Active",default=True)
    @api.depends('meals_menu.is_active')
    def _compute_active_meals(self):
        for rec in self:
            rec.active_meals = len([m for m in rec.meals_menu if m.is_active])

    @api.depends('meals_menu.is_active')
    def _compute_inactive_meals(self):
        for rec in self:
            rec.inactive_meals = len([m for m in rec.meals_menu if not m.is_active])


    @api.model_create_multi
    def create(self, vals_list):
        company = self.env.company.name
        date = fields.Date.today()

        for vals in vals_list:
            vals['name'] = f"{company}-{date}"
            vals['date']= date

        return super().create(vals_list)


    @api.model
    def archive_not_today(self):
        today = fields.Date.today()

        past = self.env['meal.menu'].search([('date',"<",today),('active','=',True)])

        for i in past:
            past.sudo().write({
                "active":False 
            })




    @api.depends('meal_plans')
    def _populate_meal_menu(self):
        for rec in self:
            current_plan_ids = rec.meal_plans.ids
            for meal_record in rec.meals_menu:
                if meal_record.meal_id.meal_plan.id not in current_plan_ids:
                    meal_record.unlink()  

            existing_records = [(4, r.id) for r in rec.meals_menu]

            new_records = []
            for plan in rec.meal_plans:
                meals = self.env['fewa.meals'].search([('meal_plan', '=', plan.id)])
                for meal in meals:
                    if meal.id not in rec.meals_menu.mapped('meal_id').ids:
                        new_records.append((0, 0, {
                            'meal_id': meal.id,
                            'is_active': True,
                        }))


            rec.meals_menu = existing_records + new_records


    def duplicate_current(self):
        self.env['meal.menu'].create({
            'date':fields.Date.today(),
            "company_id":self.company_id.id,
            "meal_plans":self.meal_plans.ids,
            'meal_plans': [(6, 0, self.meal_plans.ids)],
            "name":f"{self.env.company.name}-{fields.Date.today()}",
            "active":True

        })


class ActiveMeals(models.Model):
    _name = "active.meals"
    _description = "Active Meals"

    meal_id = fields.Many2one("fewa.meals", string="Meal", required=True)
    meal_menu = fields.Many2one("meal.menu", string="Meal Menu")
    is_active = fields.Boolean(string="Available", default=True)
    image = fields.Binary(related='meal_id.image',store=True)
    name=fields.Char(related="meal_id.name",store=True)



    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
    