from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class SisComedorBeneficiario(models.Model):
    _name = 'sis.comedor.beneficiario'
    _description = 'Beneficiarios'

    name = fields.Char(
        string='Nombres',
        required=True,
    )
    

    identificacion = fields.Char(
        string='Cédula / DNI',
        unique=True,
    )  
   
    sexo = fields.Selection([
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ], string='Sexo', required=True)
    
    edad = fields.Integer(
        string='Edad',
    )
    
    
    nacionalidad = fields.Many2one(
        'res.country',  # Modelo de país de Odoo
        string='País',
    )
    
    fecha_nacimiento = fields.Date(
        string='Fecha de nacimiento',
    )
    

     
    permanente = fields.Boolean(
        string='Permanente',
        default=False,
    )

    
    verificado = fields.Boolean(
        string='Verificado',
        default=False,
    )
      
    observaciones = fields.Text(
        string='Observaciones',
    )
    

    
    #Documento de identidad
    count_attachment = fields.Integer(
        string='Contar documentos',
        compute='_compute_count_attachment',
        store=True,
    )
        
    def _compute_count_attachment(self):
        for record in self:    
            domain = [('res_model','=',self._name), ('res_id','=',self.id)]            
            count = self.env['ir.attachment'].search_count(domain)
            record.count_attachment = count
        
    def action_view_attachment(self):
        domain = [('res_model','=',self._name), ('res_id','=',self.id)]
        action ={
            'type':'ir.actions.act_window',
            'name':'Documentos',
            'res_model':'ir.attachment',
            'view_mode':'kanban,tree,form',
            'target':'current',
            'domain':domain,
            'context':{
                'default_res_model':self._name,
                'default_res_id':self.id
                },
        } 
        return action
    
    
    @api.constrains('identificacion')
    def _check_identificacion_unique(self):
        for record in self:
            if record.identificacion:
                # Verifica si ya existe otro registro con el mismo valor
                existing_record = self.search([('identificacion', '=', record.identificacion), ('id', '!=', record.id)])
                if existing_record:
                    raise ValidationError("Ya existe un beneficiario con la misma Cédula / DNI.")
   
