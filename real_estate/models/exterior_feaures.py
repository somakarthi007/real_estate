from odoo import models, fields

class ExteriorFeatures(models.Model):
    _name = "exterior.features"
    
    exterior_feature = fields.Char(string="Exterior Feature")