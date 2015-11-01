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
        users = self.env['res.users'].search([('member', '=', True)])
        for user in users:
            print user.login
            print user.nb_part

