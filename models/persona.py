# -*- coding: utf-8 -*-
"""
 1. taller.persona
"""

from odoo import models, fields, api

class Persona(models.Model):
    _name = 'taller.persona'
    _descripcion = 'Persona genérica'

    dni = fields.Char(string="DNI", required=True)
    name = fields.Char(string="Nombre", required=True)
    direction = fields.Char(string="Dirección", required=True)
    birthDate = fields.Date(string="Fecha de nacimiento", required=True)
    