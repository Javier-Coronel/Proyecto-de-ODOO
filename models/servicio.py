from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'taller.servicio'
    _descripcion = 'Servicios relacionados con reparaciones'
    _rec_name = 'tipo'

    coste = fields.Float(string='Coste', required = True)
    tipo = fields.Selection([
        ('reponer', 'Reponer stock'),
        ('limpiado', 'Limpiado'),
        ('cristales', 'Cambiar los cristales')],
        string='Tipo de servicio', required = True)
    fecha = fields.Date(string='Fecha del servicio', required = True)