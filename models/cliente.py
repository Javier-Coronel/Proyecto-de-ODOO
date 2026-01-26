# -*- coding: utf-8 -*-
"""
 2. taller.cliente
"""

from odoo import models, fields, api

class Cliente(models.Model):
    _inherit = "taller.persona"
    _name = 'taller.cliente'
    # description no descripcion
    _description = 'Cliente del taller'

    paymentMethod = fields.Char(string="Metodo de pago", required=True)
    
    # phoneNumbre a  phoneNumber
    phoneNumber = fields.Integer(string="Telefono de contacto", required=True)
    
    registerDate = fields.Date(string="Fecha de registro", required=True)

    vehiculos_ids = fields.One2many(
        string="Vehiculos del cliente",
        comodel_name='taller.vehiculo',
        inverse_name='cliente_id'
    )

    # se te olvidó este
    num_vehiculos = fields.Integer(
        string="Total Vehículos",
        compute='_compute_num_vehiculos'
    )

    # y este
    @api.depends('vehiculos_ids')
    def _compute_num_vehiculos(self):
        for record in self:
            record.num_vehiculos = len(record.vehiculos_ids)