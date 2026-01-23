# -*- coding: utf-8 -*-
"""
 3. taller.mecanico
"""

from odoo import models, fields, api

class Mecanico(models.Model):
    _name = 'taller.mecanico'
    _descripcion = 'Trabajador del taller'

    speciality = fields.Char(string="Especialidad", required=True)
    
    position = fields.Char(string="Puesto", required=True)
    
    hireDate = fields.Date(string="Fecha de contratación", required=True)
    