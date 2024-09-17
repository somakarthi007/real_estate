from odoo import models, fields

class MaintenanceRequest(models.Model):
    _name = "property.maintenance.request"

    date_submitted = fields.Date(string="Date Submitted")
    customer_id = fields.Many2one("res.partner", string="Customer")
    property_product = fields.Many2one("product.template")
    issue_Category = fields.Selection(string="Issue Category", selection=[("Plumbing", "Plumbing"), ("Electrical", "Electrical"), ("HVAC", "HVAC"), ("Appliance", "Appliance"), ("General Maintenance", "General Maintenance")])
    description_of_issue = fields.Char(string="Description of Issue")
    priority_level = fields.Selection(string="Priority Level", selection=[("Urgent", "Urgent"), ("High", "High"), ("Medium", "Medium"), ("Low", "Low")])
    request_status = fields.Selection(string="Request Status", selection=[("Pending", "Pending"), ("In progress", "In progress"), ("Completed", "Completed"), ("On hold", "On hold")])
    scheduled_date_time = fields.Datetime(string="Scheduled Date/Time") # Send an email to confirm schedule
    assigned_technician = fields.Many2one("res.users", string="Assigned Technician") # Admin can choose the techincian, and send email to customer that a technician has been assigned
    completion_date = fields.Date(string="Completion Date")
    resolution_details = fields.Char(string="Description of the work performed")
    cost_estimate = fields.Float(string="Cost Estimate")
    actual_cost = fields.Float(string="Actual Cost")
    attachments = fields.Binary(string="Attachments")
    feedback = fields.Char(string="Feedback/Comments")
    completed_by = fields.Many2one("res.users", string="Completed By")
