from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Doctor Record"

    name = fields.Char(string="Doctor Name", required=True)
    specialty = fields.Char(string="Doctor specialty", required=True)

    patient_ids = fields.One2many(
        comodel_name="hospital.patient",
        inverse_name="doctor_id",
        string="Patients"
    )



