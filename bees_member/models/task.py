# -*- coding: utf-8 -*-

from openerp import models, fields, api


class BeesTask(models.Model):
    
    _name = "bees.task"
    
    name = fields.Char("name")
    date_start = fields.Datetime("Start")
    date_end = fields.Datetime("end")
    duration = fields.Float("Durée")
    type_id = fields.Many2one("bees.task.type", "Type")
    responsible_id = fields.Many2one("res.users", string="Responsable")
    