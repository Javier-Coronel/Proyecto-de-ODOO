# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class taller_mecanico_de_vehiculos(models.Model):
#     _name = 'taller_mecanico_de_vehiculos.taller_mecanico_de_vehiculos'
#     _description = 'taller_mecanico_de_vehiculos.taller_mecanico_de_vehiculos'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
