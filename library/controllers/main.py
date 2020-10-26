
from odoo import http
class Books(http.Controller):
	@http.route('/library/books', auth='user')#declara la ruta que vamos a dirigir a este controlador
	def list(self, **kwargs):				# el auth es un parametro que se pasa a la url
		Book = http.request.env['li.book']#obtener un grupo de registros disponibles de ese modelo
		books = Book.search([])
		print('books')
		print('books')
		print(books)
		print('books')
		print('books')
		return http.request.render('library.book_list_template', {'books': books})#para procesar la vista 

		