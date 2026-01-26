class Servicio(models.Model):
    _name = 'taller.servicio'
    _description = 'Servicios relacionados con reparaciones'
    _rec_name = 'tipo'

    coste = fields.Float(string='Coste', required=True)
    tipo = fields.Selection([
        ('reponer', 'Reponer stock'),
        ('limpiado', 'Limpiado'),
        ('cristales', 'Cambiar los cristales')
    ], string='Tipo de servicio', required=True)
    
    fecha = fields.Date(string='Fecha del servicio', required=True)

    # El campo state
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_proceso', 'En Proceso'),
        ('terminado', 'Terminado'),
        ('cancelado', 'Cancelado'),
    ], string='Estado', default='borrador', required=True)

    # Las funciones (alineadas dentro de la clase)
    def action_en_proceso(self):
        for rec in self:
            rec.state = 'en_proceso'

    def action_terminar(self):
        for rec in self:
            rec.state = 'terminado'

    def action_cancelar(self):
        for rec in self:
            rec.state = 'cancelado'
            
    def action_borrador(self):
        for rec in self:
            rec.state = 'borrador'