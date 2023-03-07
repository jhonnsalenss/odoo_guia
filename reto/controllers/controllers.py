# -*- coding: utf-8 -*-
from odoo import http


class Reto(http.Controller):
     @http.route('/reto', auth='public', website=True)
     def index(self, **kw):
         return "Hello, world"

     @http.route('/reto/reto/objects', auth='public')
     def list(self, **kw):
         return http.request.render('reto.listing', {
             'root': '/reto/reto',
             'objects': http.request.env['reto.reto'].search([]),
         })

     @http.route('/reto/reto/objects/<model("reto.reto"):obj>', auth='public')
     def object(self, obj, **kw):
         return http.request.render('reto.object', {
             'object': obj
         })
