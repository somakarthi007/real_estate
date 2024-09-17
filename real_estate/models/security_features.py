from odoo import models, fields

class SecurityFeatures(models.Model):
    _name = "security.features"
    
    security_features = fields.Char(string="Security Features")