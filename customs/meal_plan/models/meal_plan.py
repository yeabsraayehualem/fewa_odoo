from odoo import models,fields,api,_

from odoo.exceptions import ValidationError,UserError




class MealPlan(models.Model):
    _name="fewa.meal.plan"


    name = fields.Char(string="Plan Name")
    meal_ids = fields.One2many('fewa.meals','meal_plan')
    type = fields.Selection([
        ('meal', 'Meal Plan'),
        ('nutrition', 'Nutrition Plan'),
    ], string="Plan Type") 
    price = fields.Float(string="Price")
    image = fields.Binary(string="Image")
    available_orders = fields.Integer(string="Available Orders")


class Meals(models.Model):
    _name="fewa.meals"


    name = fields.Char(stirng="Name")
    image = fields.Binary(string="Image")
    meal_plan = fields.Many2one("fewa.meal.plan",string="Meal Plan")

    
