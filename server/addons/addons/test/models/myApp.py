from odoo import models,fields

class ABC (models.Model):
    _name = 'test'
    _description = 'test'

    name = fields.Char(string='name' )
    age = fields.Float(string='age' )
    image = fields.Binary(string='image')