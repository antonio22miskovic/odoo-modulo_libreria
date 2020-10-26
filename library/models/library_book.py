# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import Warning
from odoo.exceptions import ValidationError

class Book(models.Model):
	_name = 'li.book'
	_description = 'Book'
	_order = 'name, date_published desc'#ordena en froma decendete los nombre por su dato de publicación

	name = fields.Char('Title',default=None,
							index=True,
							help='Book cover title.',
							readonly=False,
							required=True,
							translate=False)

	isbn = fields.Char('ISBN')

	#tipo de libro
	book_type = fields.Selection(
		[
			('paper','Paperback'),
			('hard','Hardcover'),
			('electronic','Electronic'),
			('other', 'Other')
		],'Type')

	notes = fields.Text('Internal Notes')
	descr = fields.Html('Description')
	#fin de tipo de libro

	# Numeric fields:
	copies = fields.Integer(default=1)
	avg_rating = fields.Float('Average Rating', (3, 2))
	price = fields.Monetary('Price', 'currency_id')
	currency_id = fields.Many2one('res.currency') # price helper

	# last_borrow_date = fields.Datetime(
	# 	'Last Borrowed On',
	# 	default='_default_last	_borrow_date',
	# )

	last_borrow_date = fields.Datetime(
		'Last Borrowed On',
		default=lambda self: fields.Datetime.now(),
	)

	active = fields.Boolean('Active?', default=True)#esta propiedad funciona como el sofdelete
	date_published = fields.Date()
	image = fields.Binary('Cover')
	publisher_id = fields.Many2one('res.partner', string='Publisher')

	#editando lo que envia el captitulo 6
	publisher_country_id = fields.Many2one(
		'res.country', string='Publisher Country',
		compute='_compute_publisher_country',
		inverse='_inverse_publisher_country',
		search='_search_publisher_country',
	)

	publisher_country_related = fields.Many2one(
		'res.country', string='Publisher Country (related)',
		related='publisher_id.country_id',
	)

	author_ids = fields.Many2many('res.partner', string='Authors')


	#RESTRICCIONES (VALIDACIONES)
	_sql_constraints = [

		('library_book_name_date_uq', # Monbre del identificador
		'UNIQUE (name, date_published)', # Sentencia SQL
		'Book title and publication date must be unique.'), # Message Error

		('library_book_check_date',
		'CHECK (date_published <= current_date)',
		'Publication date must not be in the future.'),

	]


	# @api.multi
	def _check_isbn(self):# esta funcion verifica que el ultimo digito introducido sea igual a la multiplicacion de sus compañeros mediante una lista
		print(self.ensure_one())
		self.ensure_one() #verifica que sea un solo registro
		digits = [int(x) for x in self.isbn if x.isdigit()] #la funcion isdigit() comprueba que sea solo numeros
		if len(digits) == 13: #si la longitud tiene una longitud de 13 digites
			ponderations = [1, 3] * 6 #creamos una longitud de 12 digitos
			terms = [a * b for a, b in zip(digits[:12], ponderations)] # multiplica ponderacion * los digitos introducidos
			remain = sum(terms) % 10 # saca el 10% pa
			check = 10 - remain if remain != 0 else 0 #ternario para validar el resultado si es igual a 0
			print('holllaaaaaaaaalaaaaaaaaaaaa')
			print('holllaaaaaaaaalaaaaaaaaaaaa')
			print('holllaaaaaaaaalaaaaaaaaaaaa')
			print(check)
			print('holllaaaaaaaaalaaaaaaaaaaaa')
			print('holllaaaaaaaaalaaaaaaaaaaaa')
			print('holllaaaaaaaaalaaaaaaaaaaaa')
			return digits[-1] == check #si es igual return True si no return False

	# @api.multi
	def button_check_isbn(self):
		for book in self:
			if not book.isbn:
				raise Warning('Please provide an ISBN for %s' % book.name)
			if book.isbn and not book._check_isbn():
				raise Warning('%s is an invalid ISBN' % book.isbn)
		return True

	# def _default_last_borrow_date(self):
	# 	return fields.Datetime.now()

	@api.depends('publisher_id.country_id')
	def _compute_publisher_country(self):
		for book in self:
			book.publisher_country_id = book.publisher_id.country_id

	def _inverse_publisher_country(self):
		for book in self:
			book.publisher_id.country_id = book.publisher_country_id

	def _search_publisher_country(self, operator, value):
		return [('publisher_id.country_id', operator, value)]

	@api.constrains('isbn')
	def _constrain_isbn_valid(self):
		for book in self:
			if book.isbn and not book._check_isbn():
				raise ValidationError('%s is an invalid ISBN' % book.isbn)
