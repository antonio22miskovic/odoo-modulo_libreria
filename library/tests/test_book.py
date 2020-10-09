from odoo.tests.common import TransactionCase
class TestBook(TransactionCase):
	def setUp(self, *args, **kwargs):
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		result = super().setUp(*args, **kwargs)
		self.Book = self.env['li.book']
		self.book_ode = self.Book.create({
			'name': 'Odoo Development Essentials',
			'isbn': '879-1-78439-279-6'})
		return result

	def test_create(self):
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		print('testeando!!!!!!!!!!!!!!!!!!!!!!!!!')
		"Test Books are active by default"
		self.assertEqual(self.book_ode.active, True)

	def test_check_isbn(self):
		"Check valid ISBN"
		self.assertTrue(self.book_ode._check_isbn)

	def setUp(self, *args, **kwargs):
		result = super().setUp(*args, **kwargs)
		user_admin = self.env.ref('base.user_admin')
		self.env= self.env(user=user_admin)
		self.Book = self.env['li.book']
		self.book_ode = self.Book.create({
		'name': 'Odoo Development Essentials',
		'isbn': '879-1-78439-279-6'})
		return result