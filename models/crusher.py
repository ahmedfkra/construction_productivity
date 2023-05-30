from odoo import models, fields


class Crusher(models.Model):
    _name = 'crusher.model'
    _description = 'Crusher'

    name = fields.Char(string='Crusher Name')
    location = fields.Char(string='Crusher Location')
    working_sites = fields.Many2many('crusher.site', string='Working Sites')
    associated_projects = fields.Many2many('product.template', string='Associated Projects')


class CrusherSite(models.Model):
    _name = 'crusher.site'
    _description = 'CrusherSite'

    name = fields.Char()



