# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class construction_productivity(models.Model):
#     _name = 'construction_productivity.construction_productivity'
#     _description = 'construction_productivity.construction_productivity'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
