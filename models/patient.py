from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Patient Record"

    name = fields.Char(string="Patient name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    is_discharged = fields.Boolean(
        string="Discharged?",
        default=False,
        help="Check the box if the patient has completed treatment, been discharged, and left the hospital."
    )
    story = fields.Text(string="Story")

    doctor_id = fields.Many2one(
        comodel_name="hospital.doctor",
        string="Doctor",
    )

    symptom_ids = fields.Many2many(
        comodel_name="hospital.symptom",
        string="Symptoms",
    )