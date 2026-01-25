# -*- coding: utf-8 -*-
"""
 2. taller.cliente
"""

from odoo import models, fields, api

class Cliente(models.Model):
    _inherit = "taller.persona"
    _name = 'taller.cliente'
    _descripcion = 'Cliente del taller'

    paymentMethod = fields.Char(string="Metodo de pago", required=True)
    
    phoneNumbre = fields.Integer(string="Telefono de contacto", required=True)
    
    registerDate = fields.Date(string="Fecha de registro", required=True)

    vehiculos_ids = fields.One2many(
        string="Vehiculos del cliente",
        comodel_name='taller.vehiculo',
    )