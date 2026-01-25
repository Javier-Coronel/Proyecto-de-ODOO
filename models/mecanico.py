# -*- coding: utf-8 -*-
"""
 3. taller.mecanico
"""

from odoo import models, fields, api

class Mecanico(models.Model):
    _inherit = "taller.persona"
    _name = 'taller.mecanico'
    _descripcion = 'Trabajador del taller'

    speciality = fields.Char(string="Especialidad", required=True)
    
    position = fields.Char(string="Puesto", required=True)
    
    hireDate = fields.Date(string="Fecha de contratación", default=fields.Date.context_today)

    reparaciones_ids = fields.Many2many(
        string="Reparaciones",
        comodel_name='taller.orden_reparacion',
        required=True
    )
    