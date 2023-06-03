from odoo import models, fields


class Crusher(models.Model):
    _name = 'crusher.model'
    _description = 'Crusher'

    name = fields.Char(string='Crusher Name')
    location = fields.Many2one('crusher.location', string='Crusher Location')
    working_sites = fields.Many2many('crusher.site', string='Working Sites')
    work_hours = fields.Datetime(string='Work Hours')
    # operation_manger = fields.Many2one('project.worker',string='Operation Name')
    # associated_projects = fields.Many2many('product.template', string='Associated Projects')


class CrusherLocation(models.Model):
    _name = 'crusher.location'

    name = fields.Char(string='location')


class CrusherSite(models.Model):
    _name = 'crusher.site'
    _description = 'CrusherSite'

    name = fields.Char()


class ProductCrusher(models.Model):
    _name = 'crusher.product'

    name = fields.Char(string='Product')
    qu_product = fields.Float(string='Quantity Production')
    production_id = fields.Many2one('crusher.production', string='Production')


class ProductionCrusher(models.Model):
    _name = 'crusher.production'

    name = fields.Char(string='Product number')
    location = fields.Many2one('crusher.site', string='Location')
    work_hours = fields.Char(string='Working Hours')
    target_productivity = fields.Float(string='Target Productivity')
    actual_productivity = fields.Float(string='Actual Productivity')
    qu_productivity = fields.Float(string='Quantity Production')
    project_id = fields.Many2one('project.model', string='Project')
    product_id = fields.One2many('crusher.product', 'production_id', string='Product')
