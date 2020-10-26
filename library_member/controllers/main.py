from odoo import http
from odoo.addons.library.controllers.main import Books # extendemos del controlador base
class BooksExtended(Books):
	@http.route()
	def list(self, **kwargs):#extendemos a el metodo del controlador anterior
		response = super().list(**kwargs)
		print('response')
		print('response')
		print(response)
		print('response')
		print('response')
		if kwargs.get('available'):
			Book = http.request.env['li.book']
			books = Book.search([('is_available', '=', True)])
			response.qcontext['books'] = books
		return response
