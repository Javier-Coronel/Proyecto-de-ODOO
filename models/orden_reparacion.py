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
    descuento =fields.Float(string="Descuento aplicado")

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
        relation='taller_orden_mecanico_rel', 
        column1='orden_id',
        column2='mecanico_id',
        string="Mecánicos asignados"
    )

    repuestos_ids = fields.Many2many(
        comodel_name='taller.repuesto',
        relation='taller_orden_repuesto_rel',
        column1='orden_id',
        column2='repuesto_id',
        string="Repuestos utilizados"
    )

    servicios_ids = fields.Many2many(
        comodel_name='taller.servicio',
        relation='taller_orden_servicio_rel',
        column1='orden_id',
        column2='servicio_id',
        string="Servicios realizados"
    )

    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('confirmado', 'En Proceso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ], string="Estado", default='borrador')

    def action_confirmar(self):
        for record in self:
            record.state = 'confirmado'

    def action_finalizar(self):
        for record in self:
            record.state = 'finalizado'