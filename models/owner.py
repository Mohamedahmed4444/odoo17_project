from odoo import models, fields



class Owner(models.Model):
    _name= 'owner'

    name = fields.Char(required=1)
    phone = fields.Char()
    address = fields.Char()