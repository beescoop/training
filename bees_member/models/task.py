# -*- coding: utf-8 -*-

from openerp import models, fields, api
from datetime import timedelta


class BeesTask(models.Model):
    
    _name = "bees.task"
    
    name = fields.Char("name")
    date_start = fields.Datetime("Start")
    date_end = fields.Datetime("end")
    duration = fields.Float(compute="_compute_duration", inverse="_inverse_duration", string="Durée")
    type_id = fields.Many2one("bees.task.type", "Type")
    responsible_id = fields.Many2one("res.users", string="Responsable", domain=[('member', '=', True)])
    state = fields.Selection([('draft', 'Draft'), 
                              ('confirmed', 'Confirmed'), 
                              ('done', 'Done'), 
                              ('absent', 'Absent')], default='draft', readonly=True)
    
    @api.one                        
    def confirm(self):
        self.state = 'confirmed'

    @api.one                        
    def absent(self):
        self.state = 'absent'

    @api.one                        
    def done(self):
        self.state = 'done'

    @api.one
    @api.depends('date_start', 'date_end')
    def _compute_duration(self):
        if self.date_start and self.date_end:
            delta = fields.Datetime.from_string(self.date_end) - fields.Datetime.from_string(self.date_start)
            self.duration = delta.seconds / 3600.0
    
    @api.one
    def _inverse_duration(self):
        if self.date_start and self.duration:
            date_start = fields.Datetime.from_string(self.date_start)
            self.date_end = fields.Datetime.to_string(date_start + timedelta(hours=self.duration))
        
    
     
     