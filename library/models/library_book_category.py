from odoo import api, fields, models
class BookCategory(models.Model):

    _name = 'li.book.category'
    _description = 'Book Category'
    _parent_store = True

    name = fields.Char(translate=True, required=True)
    # Hierarchy fields
    parent_id = fields.Many2one(
        'li.book.category',
        'Parent Category',
        ondelete='restrict')

    parent_path = fields.Char(index=True)

    child_ids = fields.One2many(
        'li.book.category',
        'parent_id',
         string='Chils')

    highlighted_id = fields.Reference(
        [
            ('li.book', 'Book'),
            ('res.partner', 'Author')
        ],
        'Category Highlight',
    )
