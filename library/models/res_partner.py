from odoo import fields, models

class Partner(models.Model):
    """docstring forPartner."""
    _inherit = "res.partner"
    #
    published_book_ids = fields.One2many(
        'li.book',
        'publisher_id',
        string="Publisher"
    )


    # author_ids = fields.Many2many(
    #     'res.partner', string='Authors

    author_ids = fields.Many2many(
        'res.partner', # related model (required)
        relation='li_book_res_partner_rel', # relation table name
        column1='a_id', # rel table field for "this" record
        column2='p_id', # rel table field for "other" record
        string='Authors') # string label text

    book_ids = fields.Many2many(
        'li.book', string='Authored Books')
