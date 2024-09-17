{
    "name": "Real Estate",
    "version": "1.2.3",
    "description": "Estate app to keep track of properties and maintain",
    "license": "LGPL-3",
    "depends": ["base", "product", "sale"],
    "data": [
        "views/real_estate_property_view.xml",
        "views/product_template_view.xml",
        "views/maintenance_request_website_view.xml",
        "views/maintenance_request_list_view.xml",
        # "views/property_listing_custom_list_view.xml",
        # "views/property_listing_custom_form_view.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installation": True
}