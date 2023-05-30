from odoo import fields, models, api


class MixerManagement(models.Model):
    _name = 'mixer.model'
    _description = 'Mixer Model'

    name = fields.Char(string='Mixer')
    no_mixer = fields.Char(string='Mixer Number')
    type = fields.Many2one('mixer.type', string='Type')
    status = fields.Selection([('operation', 'Operation'), ('manitence', 'Manitence'), ('stop', 'Stop')])
    last_maintence = fields.Date(string='Last Manitence')
    purchase_date = fields.Date(string='Purchase Date')
    hours_work = fields.Integer(string='Hours Date')
    production_ids = fields.One2many('mixer.production', 'mixer_id', string='الإنتاجية')
    capacity = fields.Float(string='السعة')
    manufacturer = fields.Char(string='الشركة المصنعة')
    location = fields.Char(string='الموقع')
    category_id = fields.Many2one('mixer.category', string='التصنيف')
    supplier_id = fields.Many2one('mixer.supplier')




class Production(models.Model):
    _name = 'mixer.production'

    name = fields.Char(string='اسم الإنتاجية')
    units = fields.Float(string='units')
    units_total = fields.Integer(string='إجمالي الوحدات' , compute= 'compute_total_unit')
    units_completed = fields.Integer(string='الوحدات المكتملة')
    progress = fields.Float(string='نسبة التقدم', compute='compute_progress')
    mixer_id = fields.Many2one('mixer.model', string='الخلاطة')
    start_time = fields.Date(string='تاريخ البدء')
    end_time = fields.Date(string='تاريخ الانتهاء')
    is_completed = fields.Boolean(string='تم الانتهاء')
    projects_id = fields.Many2one('project.model', string='Project')
    # duration = fields.Float(string='المدة', compute='_compute_duration')

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for production in self:
            if production.start_time and production.end_time:
                duration = (production.end_time - production.start_time).total_seconds() / 3600
                production.duration = duration

    @api.depends('units')
    def compute_total_unit(self):
        for rec in self:
            rec.units_total = rec.units

    @api.onchange('units')
    def onchange_unit(self):
        if self.units < 0:
            raise UserWarning('you cannot productivity zero')

    @api.depends('units_total', 'units_completed')
    def compute_progress(self):
        for production in self:
            if production.units_total:
                progress = (production.units_completed / production.units_total) * 100
                production.progress = progress
            else:
                production.progress = 0.0



class Supplier(models.Model):
    _name = 'mixer.supplier'

    name = fields.Char(string='اسم المورد')
    mixer_ids = fields.One2many('mixer.model', 'supplier_id', string='الخلاطات')


class MaintenanceTechnician(models.Model):
    _name = 'mixer.maintenance_technician'

    name = fields.Char(string='اسم الفني')
    mixer_ids = fields.Many2many('mixer.model', string='الخلاطات')


class Engineer(models.Model):
    _name = 'mixer.engineer'

    name = fields.Char(string='اسم المهندس')
    mixer_ids = fields.Many2many('mixer.model', string='الخلاطات')


class MixerType(models.Model):
    _name = 'mixer.type'

    name = fields.Char()


class MixerCategory(models.Model):
    _name = 'mixer.category'

    name = fields.Char(string='اسم التصنيف')