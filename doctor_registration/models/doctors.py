from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    
    name = fields.Char(string='Doctor Name')
    cnic = fields.Char(string='CNIC')
    mobile_no = fields.Char(string='Mobile No')
    email = fields.Char(string='Email')
