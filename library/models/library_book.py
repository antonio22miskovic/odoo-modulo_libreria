# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning

class Book(models.Model):
	_name = 'li.book'
	_description = 'Book'
	
	name = fields.Char('Title', required=True)
	isbn = fields.Char('ISBN')
	active = fields.Boolean('Active?', default=True)#esta propiedad funciona como el sofdelete
	date_published = fields.Date()
	image = fields.Binary('Cover')
	publisher_id = fields.Many2one('res.partner', string='Publisher')
	author_ids = fields.Many2many('res.partner', string='Authors')

	# @api.multi
	def _check_isbn(self):# esta funcion verifica que el ultimo digito introducido sea igual a la multiplicacion de sus compañeros mediante una lista

		print("_check_isbnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
		print(self.ensure_one())
		print("_check_isbnnnnnnnnnnnnnnnnnnnnnnnnnnnn")

		self.ensure_one() #verifica que sea un solo registro
		digits = [int(x) for x in self.isbn if x.isdigit()] #la funcion isdigit() comprueba que sea solo numeros
		print('resultado de digits')
		print(digits)
		print('resultado de digits')

		if len(digits) == 13: #si la longitud tiene una longitud de 13 digites 
			ponderations = [1, 3] * 6 #creamos una longitud de 12 digitos

			print('resultado de ponderations')
			print(ponderations)
			print('resultado de ponderations')

			terms = [a * b for a, b in zip(digits[:12], ponderations)] # multiplica ponderacion * los digitos introducidos

			print('resultado de term')
			print(terms)
			print('resultado de term')

			remain = sum(terms) % 10 # saca el 10% pa

			print('resultado de remain')
			print(remain)
			print('resultado de remain')

			check = 10 - remain if remain != 0 else 0 #ternario para validar el resultado si es igual a 0

			print('resultado de check')
			print(check)
			print('resultado de check')
			print('digits[-1]')
			print(digits[-1])
			r =digits[-1] == check
			print ('print r')
			print (r)
			print ('print r')
			return digits[-1] == check #si es igual return True si no return False

   
	# # @api.multi
	def button_check_isbn(self):
		print('se esta ejecutando el metodo button')
		print('se esta ejecutando el metodo button')
	
		for book in self:
			if not book.isbn:
				raise Warning('Please provide an ISBN for %s' % book.name)
			if book.isbn and not book._check_isbn():
				raise Warning('%s is an invalid ISBN' % book.isbn)
		return True