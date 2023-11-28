
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SisComedorAsistencia(models.Model):
    _name = 'sis.comedor.asistencia'
    _description = 'Asistencia'

    fecha = fields.Date(
        string='Fecha de hoy',
        default=fields.Date.context_today,
        required=True
    )
    
    nota = fields.Char(
        string='Nota',
    )
    
    
    numero = fields.Integer(
        string='Número',
    )
    
    
    beneficiarios_ids = fields.Many2many(
        comodel_name='sis.comedor.beneficiario',
        relation='sis_comedor_asistencia_beneficiario_rel',
        column1='asistencia_id',
        column2='beneficiario_id',
        string='Beneficiarios',
    )