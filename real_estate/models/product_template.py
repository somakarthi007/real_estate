from odoo import models, fields, api
import datetime

class ProductTemplate(models.Model):
    _inherit = "product.template"

     # Basic Property Information
    is_real_estate_product = fields.Boolean(string="Real Estate Product", default=False)
    property_type = fields.Selection(string="Type of property", selection=[("Residential","Residential") , ("Commercial", "Commercial"), ("Industrial", "Industrial")])
    street_address = fields.Char(string="Street Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State/Province")
    postal_code = fields.Char(string="Zip/Postal Code")
    country = fields.Char(string="Country")
    neighborhood = fields.Char(string="Name of the neighborhood or community")
    description = fields.Char(string="A brief description of the property")

    # Physical Characteristics
    building_type = fields.Selection(string="Building Type", selection=[("Single-family", "Single-family"), ("Multi-family", "Multi-family"), ("Condo", "Condo"), ("Office building", "Office building")])
    construction_year = fields.Date(string="Year the property was built")
    total_area = fields.Float(string="Total Area")
    number_of_floors = fields.Integer(string="Total number of floors in the building")
    number_of_units = fields.Integer(string="Number of individual units")
    unit_size = fields.Float(string="Size of each unit")
    bedrooms = fields.Integer(string="Number of bedrooms")
    bathrooms = fields.Integer(string="Number of bathrooms")
    parking = fields.Integer(string="Number of parking spaces or type of parking")

    # Features and Amenities
    heating_cooling = fields.Selection(string="Heating/Cooling", selection=[("Central Air", "Central Air"), ("HVAC", "HVAC"), ("Radiant Heat", "Radiant Heat")])
    applicances_included = fields.Many2many("appliances.included", string="Appliances Included")
    flooring = fields.Char(string="Flooring")
    interior_features = fields.Many2many("interior.features", string="Interior Features")
    exterior_features = fields.Many2many("exterior.features", string="Exterior Features")
    security_features = fields.Many2many("security.features", string="Security Features")

    # Status and Availability:
    status = fields.Selection(string="Status", selection=[("For Sale", "For Sale"), ("For Rent", "For Rent"), ("Sold", "Sold"), ("Leased", "Leased")])
    availability_date = fields.Date(string="Availability Date")
    occupancy_status = fields.Selection(string="Current occupancy status", selection=[("Occupied", "Occupied"), ("Vacant", "Vacant")])


    # Additional Information
    photos = fields.Binary(string="Photos", attachment=True)
    floor_plans = fields.Binary(string="Floor Plans", attachment=True)
    virtual_tours = fields.Char(string="Tour Link")
    # agent_model_id = fields.Many2one("res.users", string="Agent", default=lambda self: self.env.user)
    agent_model_id = fields.Many2one("res.users", string="Agent")
    # buyer = fields.Many2one("res.partner", string="Buyer", readonly=True, copy=False)
    buyer_model_id = fields.Many2one("res.partner", string="Buyer")
    notes = fields.Char(string="Notes")

    


    