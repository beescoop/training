# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BeesMember(models.Model):
    _inherit = "res.users"
    
    member = fields.Boolean()
    allow_task_type_ids = fields.Many2many('bees.task.type')
    nb_part = fields.Integer('Nombre de part')
    part_type = fields.Selection([('a', 'Part active'), ('b', 'Personne Morale'),  ('c', 'Personne de soutien')])
    
