# -*- coding: utf-8 -*-
"""
 2. taller.cliente
"""

from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'taller.cliente'
    _descripcion = 'Cliente del taller'

    speciality = fields.Char(string="Especialidad", required=True)
    
    position = fields.Char(string="Puesto", required=True)
    
    hireDate = fields.Date(string="Fecha de contratación", required=True)
    