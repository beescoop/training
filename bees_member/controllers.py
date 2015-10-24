# -*- coding: utf-8 -*-
from openerp import http

# class BeesMember(http.Controller):
#     @http.route('/bees_member/bees_member/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bees_member/bees_member/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bees_member.listing', {
#             'root': '/bees_member/bees_member',
#             'objects': http.request.env['bees_member.bees_member'].search([]),
#         })

#     @http.route('/bees_member/bees_member/objects/<model("bees_member.bees_member"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bees_member.object', {
#             'object': obj
#         })