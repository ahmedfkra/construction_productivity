from odoo import models, fields, api


# Cursher


class Crusher(models.Model):
    _name = 'crusher.model'
    _description = 'Crusher'

    name = fields.Char(string='Crusher Name')
    location = fields.Many2one('crusher.site', string='Crusher Location')
    working_sites = fields.Many2many('crusher.site', string='Working Sites')
    work_hours = fields.Datetime(string='Work Hours')
    capacity = fields.Integer(string='Capacity')
    product = fields.One2many('crusher.product', 'crusher', string='Product')
    # operation_manger = fields.Many2one('project.worker',string='Operation Name')
    # associated_projects = fields.Many2many('product.template', string='Associated Projects')


class CrusherLocation(models.Model):
    _name = 'crusher.location'

    name = fields.Char(string='location')


# cursher site


class CrusherSite(models.Model):
    _name = 'crusher.site'
    _description = 'CrusherSite'

    name = fields.Char()
    area = fields.Selection([('وسط', ' المنطقة الوسطي'), ('شرق', ' المنطقة الشرقية'), ('غرب', ' المنطقة الغربية')],
                            string='My Selection Field')


# crusher production


class ProductCrusher(models.Model):
    _name = 'crusher.product'

    name = fields.Char(string='Product')
    qu_product = fields.Float(string='Quantity Production')
    production_id = fields.Many2one('crusher.production', string='Production')
    crusher = fields.Many2one('crusher.model', string='Crusher')


class ProductionCrusher(models.Model):
    _name = 'crusher.production'

    name = fields.Char(string='Product number')
    location = fields.Many2one('crusher.site', string='Location')
    work_hours = fields.Float(string='Working Hours')
    target_productivity = fields.Float(string='Target Productivity')
    actual_productivity = fields.Float(string='Actual Productivity')
    qu_productivity = fields.Float(string='Quantity Production')
    project_id = fields.Many2one('project.model', string='Project')
    product_id = fields.Many2many('crusher.product', string='Product')

    # compute field
    crusher_production = fields.Float(string='إنتاجية الكسارة', compute='compute_crusher_production')
    production_rate = fields.Float(string='معدل إنتاج الكسارة', compute='compute_production_rate')
    production_efficiency = fields.Float(string='نسبة إنتاج الكسارة', compute='compute_production_efficiency')

    @api.depends('crusher_production')
    def compute_crusher_production(self):
        for rec in self:
            rec.crusher_production = rec.production_rate * rec.production_efficiency


    @api.depends('production_rate')
    def compute_production_rate(self):
        for rec in self:
            if rec.work_hours != 0:
                rec.production_rate = rec.qu_productivity / rec.work_hours

    @api.depends('production_efficiency')
    def compute_production_efficiency(self):
        for rec in self:
            if rec.target_productivity != 0:
                rec.production_efficiency = (rec.actual_productivity / rec.target_productivity) * 100

