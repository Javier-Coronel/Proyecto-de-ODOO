from odoo import models, fields, api

class Repuesto(models.Model):
    _name = 'taller.repuesto'
    _descripcion = 'Piezas de repuesto'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required = True)
    coste = fields.Float(string='Coste', required = True)
    tipo = fields.Selection([
        ('neumaticos', 'Neumáticos'),
        ('limpiaparabrisas', 'Limpiaparabrisas'),
        ('motores', 'Motores')],
        string='Tipo de componente', required = True)
    fecha = fields.Date(string='Fecha de compra', required = True)