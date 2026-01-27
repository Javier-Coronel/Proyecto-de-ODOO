# -*- coding: utf-8 -*-
"""
 3. taller.mecanico
"""

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class Mecanico(models.Model):
    _inherit = "taller.persona"
    _name = 'taller.mecanico'
    _descripcion = 'Trabajador del taller'
    speciality = fields.Selection([
        ('engine','Motor'),
        ('chassis','Chasis'),
        ('tire','Neumáticos')
        ],
        string="Especialidad", 
        required=True)
    
    position = fields.Char(string="Puesto", required=True)
    
    hireDate = fields.Date(string="Fecha de contratación", default=fields.Date.context_today, )

    reparaciones_ids = fields.Many2many(
        string="Reparaciones",
        comodel_name='taller.orden_reparacion',
        required=True
    )
    
    reparaciones_monthly = fields.Integer(
        string="Reparaciones hechas al mes",
        compute='_compute_reparaciones_monthly'
    )

    @api.constrains('hireDate')
    def _check_hireDate(self):
        for record in self:
            if record.hireDate > fields.Date.today():
                raise ValidationError("La fecha de contratacion no puede ser del futuro")

    @api.depends('reparaciones_ids', 'hireDate')
    def _compute_reparaciones_monthly(self):
        for record in self:
            num_reparations = len(record.reparaciones_ids)
            months =  (record.hireDate.year - date.today().year) * 12 + record.hireDate.month - date.today().month + 1
            record.reparaciones_monthly = num_reparations / months
    