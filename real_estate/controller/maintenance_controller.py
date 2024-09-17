from odoo import http
from odoo.http import request
from datetime import date
import werkzeug

class MaintenanceController(http.Controller):


    @http.route("/maintenance-request", auth="user", website=True)
    def maintenance_request_index(self):

        data = {}

        partner_id = 0
        # Get Current Logged in User
        customer_id = request.session.uid

        print("customer_id: " + str(customer_id))

        # Get partner_id (customer ref) from res.users (logged in user)
        users = request.env["res.users"].search([("id", "=", customer_id)])
        print("users: " + str(users))
        for user in users:
            partner_id = user.partner_id.id
            break     

        print("partner_id: " + str(partner_id))
        # Maintenance Requests of current logged in user
        maintenance_requests = request.env["property.maintenance.request"].search([("customer_id", "=", partner_id)])
        # maintenance_requests.sorted(lambda o: o.create_date, reverse=True)

        if "message" in request.session:
            data["message"] = request.session['message']
        data["maintenance_requests"] = maintenance_requests

        print("data: " + str(data))

        return request.render("real_estate.all_maintenance_request_template", data)


    @http.route("/maintenance-request-form", auth="user", website=True)
    def maintenance_request_form(self):
        # set message to empty
        request.session['message'] = ""      
        
        maintenance_request = {}

        # Get Current Logged in User
        customer_id = request.session.uid

        # print("customer_id: " + str(customer_id))

        # Get partner_id (customer ref) from res.users (logged in user)
        users = request.env["res.users"].search([("id", "=", customer_id)])
        for user in users:
            if maintenance_request.get("customer_id") == None:
                maintenance_request["customer_id"] = user.partner_id.id
                break
        
        # real estate website orders of the current logged in user
        sales_orders = request.env["sale.order"].search([("website_id", "=", 3), ("partner_id", "=", maintenance_request.get("customer_id"))])
        # print("sales_orders: " + str(sales_orders))

        product_template_ids = []
        
        for sales_order in sales_orders:
            # print("Order " + str(sales_order.name))
            for order_line in sales_order.order_line:
                print(str(order_line.product_template_id.id))
                product_template_ids.append(order_line.product_template_id.id)

        #  Fetch all real estate products customer has ordered
        real_estate_products = request.env["product.template"].search([("id", "in", product_template_ids)])
        # print(real_estate_products)

        maintenance_request["property_product"] = real_estate_products
    
        print("maintenance_request: " + str(maintenance_request))
        return request.render("real_estate.maintenance_request_form_template", maintenance_request)


    @http.route("/create-maintenance-request", auth="user", website=True, methods=["POST"])
    def maintenance_request(self, **kw):
         # set message to empty
        request.session['message'] = ""

        maintenance_request = kw
        maintenance_request["date_submitted"] = date.today()
        maintenance_request["request_status"] = "Pending"
        print("maintenance_request: " + str(maintenance_request))
        request.env["property.maintenance.request"].sudo().create(maintenance_request)
        # Show thanks for submitting message
        request.session['message']= "Thanks for submitting!"
        # Send an email stating, We have recieved your maintenance request, status: "Pending", We will assign a technician soon and notify you to schedule to perform maintenance
        return werkzeug.utils.redirect("/maintenance-request")