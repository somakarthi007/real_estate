from odoo import models, fields

class AppliancesIncluded(models.Model):
    _name = "appliances.included"
    
    appliance = fields.Char(string="Appliance")