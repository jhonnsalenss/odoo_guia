# -*- coding: utf-8 -*-
# from odoo import http


# class Nuevomodulo(http.Controller):
#     @http.route('/nuevomodulo/nuevomodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nuevomodulo/nuevomodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('nuevomodulo.listing', {
#             'root': '/nuevomodulo/nuevomodulo',
#             'objects': http.request.env['nuevomodulo.nuevomodulo'].search([]),
#         })

#     @http.route('/nuevomodulo/nuevomodulo/objects/<model("nuevomodulo.nuevomodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nuevomodulo.object', {
#             'object': obj
#         })
