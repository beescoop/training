# -*- coding: utf-8 -*-

from openerp import models, fields, api


class ProductColor(models.Model):
    _name = "product.color"
    
    name = fields.Char()
    color_code = fields.Char("Color Code")
    
class BeesProduct(models.Model):
    _inherit = "product.template"
    
    bio = fields.Many2one('product.color', 'Bio')
    local = fields.Many2one('product.color', 'Local')
    fair_trade = fields.Many2one('product.color', 'Fair Trade')

    @api.one
    def copy_from_category(self):
        print self.categ_id.bio
        print self.categ_id.fair_trade
        self.bio = self.categ_id.bio
        self.local = self.categ_id.local
        self.fair_trade = self.categ_id.fair_trade
    
class BeesCategory(models.Model):
    
    _inherit = "product.category" 
    
    bio = fields.Many2one('product.color', 'Bio')
    local = fields.Many2one('product.color', 'Local')
    fair_trade = fields.Many2one('product.color', 'Fair Trade')
    
    
