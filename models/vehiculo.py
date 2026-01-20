# -*- coding: utf-8 -*-
"""
 4. taller.vehiculo (Coche/Moto con matrícula y bastidor)
"""

from odoo import models, fields, api

class vehiculo(models.Model):
    _name= 'taller_mecanico_de_vehiculos.vehiculo'
    _description = 'Vehículo a reparar'

    matricula = fields.Char(string="Matrícula", required=True)
    numbastidor = fields.Char(string="Número de Bastidor (VIN)", required=True)

    vehicle_type = fields.Selection(
        selection=[
            ('car', 'Coche'),
            ('motorcycle', 'Moto')
        ],
        string="Tipo de Vehículo",
        required=True,
        default='car'
    )

    fecha_compra=fields.Date(
        string='Fecha de la compra del vehículo',
        default=fields.Date.today
    )

    num_reparaciones=fields.Integer(
        compute='_compute_num_reparaciones' )
    
    repair_ids=fields.One2many(
        string='Reparaciones',
        comodel_name='taller_mecanico_de_vehiculos.reparacion',
        inverse_name='vehiculo_id'
    )

    cliente_id=fields.Many2one(
        string='Clientes',
        comodel_name='taller_mecanico_de_vehiculos.cliente',
        ondelete='restrict',
    )

    @api.depends('reparaciones_ids')
    def _compute_num_reparaciones(self):
        for record in self:
            record.num_reparaciones = len(record.reparaciones_ids)