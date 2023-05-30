# -*- coding: utf-8 -*-
# from odoo import http


# class ConstructionProductivity(http.Controller):
#     @http.route('/construction_productivity/construction_productivity', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/construction_productivity/construction_productivity/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('construction_productivity.listing', {
#             'root': '/construction_productivity/construction_productivity',
#             'objects': http.request.env['construction_productivity.construction_productivity'].search([]),
#         })

#     @http.route('/construction_productivity/construction_productivity/objects/<model("construction_productivity.construction_productivity"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('construction_productivity.object', {
#             'object': obj
#         })
