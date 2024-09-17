from odoo import http
from odoo.http import request

class FileController(http.Controller):

    # @http.route("/file/template", auth="public", website=True)
    @http.route("/soma", auth="public")
    def show_property_images(self):
        # real estate website orders
        sales_orders = request.env["sale.order"].search([("website_id", "=", 3)])
        # sales_orders = request.env["sale.order"].search([])
        # print(sales_orders)
        salesOrderLineToSalesOrderMapping = {}
        productToSalesOrderLineMapping = {}
        salesOrders = {}

        final_list_real_estate_orders = []

        for sales_order in sales_orders:
            salesOrders[sales_order.id] = sales_order
            print("Order " + str(sales_order.name))
            for order_line in sales_order.order_line:
                # print("Order Line: " + str(order_line.id) + str(order_line.name))
                # print("Order Line Product: " + str(order_line.product_template_id))
                salesOrderLineToSalesOrderMapping[order_line.id] = sales_order.id
                # Order lines may appear with same product template, so only consider the first to appear
                if productToSalesOrderLineMapping.get(order_line.product_template_id.id) == None:
                    productToSalesOrderLineMapping[order_line.product_template_id.id] = order_line.id

        # print(str(productToSalesOrderLineMapping))


        #  Fetch all real estate products
        real_estate_products = request.env["product.template"].search([("is_real_estate_product", "=", "True")])
        # print(real_estate_products)


        for real_estate_product in real_estate_products:
             # Supply Product Id to get Order Line
             if productToSalesOrderLineMapping.get(real_estate_product.id) != None:
                # Supply Order Line to get Order
                if salesOrderLineToSalesOrderMapping.get(productToSalesOrderLineMapping.get(real_estate_product.id)) != None:
                    sales_order_id = salesOrderLineToSalesOrderMapping.get(productToSalesOrderLineMapping.get(real_estate_product.id))
                    sales_order = salesOrders[sales_order_id]
                    final_list_real_estate_orders.append(sales_order)
                    # print("Property Sales Order: " + str(sales_order.name))
           
        return str(final_list_real_estate_orders)
