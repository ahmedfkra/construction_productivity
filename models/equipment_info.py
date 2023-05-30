from odoo import fields, models, api


class EquipmentInfo(models.Model):
    _name = 'equipment.info'
    _description = 'EquipmentInfo'

    name = fields.Char()
    no_equipment = fields.Char(string='Number of Equipment')
    type_equipment = fields.Many2one('equipment.type', string='Type Equipment')


class EquipmentProductivity(models.Model):
    _name = 'equipment.productivity'
    _description = 'EquipmentProductivity'

    equ_name = fields.Many2one('equipment.info', string='Equipment Name')
    actual_productivity = fields.Float('Actual Productivity')
    target_productivity = fields.Float('Target Productivity')
    work_hours = fields.Integer('Work Hours')
    over_time = fields.Float(string='Over Time')
    all_working_hours = fields.Float(string='إجمالي عدد الساعات')
    achieved_rate = fields.Float(compute='compute_achieved_rate')
    project_id = fields.Many2one('project.model',string='إسم المشروع')
    units = fields.Float(string='units')
    units_total = fields.Integer(string='إجمالي الوحدات', compute='compute_total_eq_unit')

    @api.depends('units')
    def compute_total_eq_unit(self):
        for rec in self:
            rec.units_total = rec.units

    @api.onchange('units')
    def onchange_unit(self):
        if self.units < 0:
            raise UserWarning('you cannot productivity zero')


    @api.depends('achieved_rate')
    def compute_achieved_rate(self):
        for rec in self:
            ac = (rec.actual_productivity / rec.target_productivity) * 100
            rec.achieved_rate = ac


class EquipmentType(models.Model):
    _name = 'equipment.type'
    _description = 'EquipmentType'

    name = fields.Char()
