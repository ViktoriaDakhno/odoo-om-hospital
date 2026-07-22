from odoo import api, fields, models


class HospitalSymptom(models.Model):
    _name = 'hospital.symptom'
    _description = "Patient Symptom"

    name = fields.Char(string="Symptom Name", required=True)
