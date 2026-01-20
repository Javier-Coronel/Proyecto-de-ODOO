# -*- coding: utf-8 -*-
"""
 5.taller.orden_reparacion (Documento principal de trabajo) 
"""

from odoo import models, fields, api

class orden_reparacion(models.Model):
    _name = 'taller.orden_reparacion'
    _description = 'Orden de Reparación'

    nombrepieza = fields.Char(string="Nombre de pieza", required=True)
    coste =fields.Float(string="Coste de la pieza", required=True)
    descuento =fields.Float(string="Descuento aplicado", required=False)

    fecha_reparacion = fields.Date(
        string='Fecha de la reparación del vehículo',
        default=fields.Date.context_today
    )

    vehiculo_id = fields.Many2one(
        comodel_name='taller.vehiculo',
        string="Vehículo",
        required=True
    )

    mecanicos_ids = fields.Many2many(
        comodel_name='taller.mecanico',
        string="Mecánicos asignados"
    )

    repuestos_ids = fields.Many2many(
        comodel_name='taller.repuesto',
        string="Repuestos utilizados"
    )