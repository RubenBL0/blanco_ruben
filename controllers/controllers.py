# -*- coding: utf-8 -*-
# from odoo import http


# class BlancoRuben(http.Controller):
#     @http.route('/blanco_ruben/blanco_ruben/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/blanco_ruben/blanco_ruben/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('blanco_ruben.listing', {
#             'root': '/blanco_ruben/blanco_ruben',
#             'objects': http.request.env['blanco_ruben.blanco_ruben'].search([]),
#         })

#     @http.route('/blanco_ruben/blanco_ruben/objects/<model("blanco_ruben.blanco_ruben"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('blanco_ruben.object', {
#             'object': obj
#         })
