# -*- coding: utf-8 -*-
from odoo import http

# class AddonsLibrary/library(http.Controller):
#     @http.route('/addons_library/library/addons_library/library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons_library/library/addons_library/library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons_library/library.listing', {
#             'root': '/addons_library/library/addons_library/library',
#             'objects': http.request.env['addons_library/library.addons_library/library'].search([]),
#         })

#     @http.route('/addons_library/library/addons_library/library/objects/<model("addons_library/library.addons_library/library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons_library/library.object', {
#             'object': obj
#         })