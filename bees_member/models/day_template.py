# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import datetime, timedelta


class BeesTaskTemplate(models.Model):
    _name = 'bees.task_template'

    _rec_name = 'type_id'

    type_id = fields.Many2one('bees.task.type', "Task Type", required=True)
    day_id = fields.Many2one('bees.day_template', required=True)
    number = fields.Integer(required=True)
    duration = fields.Float(required=True)


class BeesDayTemplate(models.Model):
    _name = 'bees.day_template'

    name = fields.Char()
    template_ids = fields.One2many("bees.task_template", "day_id")

    @api.multi
    def generate_task(self):
        task_ids = []
        task_env = self.env["bees.task"]
        for template in self.template_ids:
            for _ in xrange(0, template.number):
                task_data = {
                    'name': template.type_id.name,
                    'date_start': fields.Datetime.now(),
                    'date_end': fields.Datetime.to_string(datetime.now() + timedelta(hours=template.duration)),
                    'duration': template.duration,
                    'type_id':  template.type_id.id,
                    'state': 'draft',
                }
                task = task_env.create(task_data)
                task_ids.append(task.id)

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bees.task',
            'view_mode': 'tree,form',
            'view_type': 'form',
            'target': 'current',
            'domain': [('id', 'in', task_ids)]
        }
