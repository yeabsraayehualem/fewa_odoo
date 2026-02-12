from odoo import models,fields,api,_



class ResUsers(models.Model):
    _inherit="res.users"


    user_type = fields.Selection(
        [('employee',"Employee"),("self_employed","Self Employed")], string="User Type"
    )
    