from odoo import models, fields, api

class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Real Estate Property Details"
    # _inherits = "product.template"

    # Basic Property Information
    property_name = fields.Char(string="Name or title of the property",)
    property_type = fields.Selection(string="Type of property", selection=[("Residential","Residential") , ("Commercial", "Commercial"), ("Industrial", "Industrial")])
    street_address = fields.Char(string="Street Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State/Province")
    postal_code = fields.Char(string="Zip/Postal Code")
    country = fields.Char(string="Country")
    neighborhood = fields.Char(string="Name of the neighborhood or community")
    description = fields.Char(string="A brief description of the property")

    # Physical Characteristics
    building_type = fields.Char(string="Building Type")
    construction_year = fields.Integer(string="Property Value")
    total_area = fields.Float(string="Total Area")
    number_of_floors = fields.Integer(string="Total number of floors in the building")
    number_of_units = fields.Integer(string="Number of individual units")
    unit_size = fields.Float(string="Size of each unit")
    bedrooms = fields.Integer(string="Number of bedrooms")
    bathrooms = fields.Integer(string="Number of bathrooms")
    parking = fields.Integer(string="Number of parking spaces or type of parking")

#     # Features and Amenities
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")
#     city = fields.Char(string="City")

    # Financial Information:
    listing_price = fields.Float(string="Listing Price")
    rental_price = fields.Float(string="Rental Price")
    property_taxes = fields.Float(string="Property Taxes")
    insurance_cost = fields.Float(string="Insurance Cost")


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

    # Link Property to a Product
    # product_model_id = fields.Many2one('product.template', string='Product', required=True, ondelete="cascade")
    product_model_id = fields.Many2one('product.template', string='Product', required=False)

    @api.model
    def create(self, vals):
        purchase_ok = False
        if(vals["status"] == "For Sale"):
            purchase_ok = True
        product_model_id = self.env["product.template"].create({"name": vals["property_name"], "description_sale": vals["description"], "list_price": vals["listing_price"], "standard_price": vals["listing_price"], "purchase_ok":  purchase_ok})
        vals["product_model_id"] = product_model_id.id
        res = super(RealEstateProperty, self).create(vals)
        return res