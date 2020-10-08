# -*- coding: utf-8 -*-

from odoo import models, fields, api

class library(models.Model):
    _name = 'li.library'

    titulo = fields.Char(string="Titulo",required=True)
    autor = fields.Char(string="Autor",required=True)
    compania = fields.Char(string="Compañia de Publicacion",required=True)
    fecha_publicacion = fields.Date(string='Fecha de publicacion',required=True)
    isbn = fields.Integer(string='ISBN',required=True, size=10, help='maximo 10 digitos')
    image = fields.Binary('Portada')



   