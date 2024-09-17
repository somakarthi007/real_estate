from odoo import models, fields

class InteriorFeatures(models.Model):
    _name = "interior.features"
    
    interior_feature = fields.Char(string="Interior Feature")