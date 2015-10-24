# -*- coding: utf-8 -*-

from openerp import models, fields, api

class BeesTaskType(models.Model):
	
	_name = 'bees.task.type' #=> psql bees_task_type
	
	name = fields.Char("Name", required=True)
	description = fields.Html("Description")
	task_ids = fields.One2many("bees.task", "type_id")
	allow_user_ids = fields.Many2many('res.users', string="Allow Users")



