from odoo import fields, models, api


class ProjectModel(models.Model):
    _name = 'project.model'
    _description = 'Construction Projects'

    name = fields.Char(string='إسم المشروع')
    desc_project = fields.Text(string="وصف المشروع")
    start_date = fields.Date(string='بداية المشروع')
    End_date = fields.Date(string='نهاية المشروع')
    cost = fields.Float(string='تكلفة المشروع')
    total_unit = fields.Float(string='إنتاجية الخلاطات',compute='compute_total_unit')
    total_unit_equ = fields.Float(string='إنتاجية المعدات ',compute='compute_total_equ_unit')
    hours_plan = fields.Integer(string='Hours Plan')
    work_plan = fields.Integer(string='Work Plan')
    production_id = fields.One2many('mixer.production','projects_id',string='Production')
    production_equ_id = fields.One2many('equipment.productivity','project_id',string='Production Equipment')
    # actual_plan = fields.Integer(string='Actual Plan')
    # quantity_plan = fields.Integer(string='Quantity Plan', compute='_compute_quantity_plan')
    # quantity_cost = fields.Integer(string='Quantity Cost')
    # actual_cost = fields.Integer(string='Actually Cost')
    # state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done')])

    item_count = fields.Integer(string='بنود المشروع', compute='compute_item_count')

    # Relationship
    items = fields.One2many('project.item', 'project_id', string='Project Items')
    equipment = fields.One2many('project.item', 'project_id', string='Project Items')

    @api.depends('items')
    def compute_item_count(self):
        for rec in self:
            rec.item_count = len(rec.items)

    @api.depends('production_id.units')
    def compute_total_unit(self):
        for rec in self:
            rec.total_unit = sum(rec.production_id.mapped('units'))

    @api.depends('production_equ_id.units')
    def compute_total_equ_unit(self):
        for rec in self:
            rec.total_unit_equ = sum(rec.production_equ_id.mapped('units'))


class ProjectItem(models.Model):
    _name = 'project.item'
    _description = 'ProjectItems'

    name = fields.Char(string='Item Name', required=True)
    item_number = fields.Char(string='Item Number', required=True)
    unit_of_measurement = fields.Char(string='Unit of Measurement', required=True)
    construction_name = fields.Char(string='Construction Name', required=True)
    quantity = fields.Float(string='Quantity', required=True)
    stages = fields.One2many('project.stages', 'item_id', string='Stages', )
    project_id = fields.Many2one('project.model', string='Project', required=True)

    def open_create_stage_form(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Stage',
            'res_model': 'project.stages',
            'view_mode': 'tree',
            'target': 'new',
            'context': {
                'default_item_id': self.id
            }
        }


class ProjectStage(models.Model):
    _name = 'project.stages'
    _description = 'ProjectStage'

    name = fields.Char(string='Stage Name', required=True)
    item_id = fields.Many2one('project.item', string='Project Item')
    tasks = fields.One2many('project.tasks', 'stage_id', string='Tasks')
    # اخر التعديلات
    product_id = fields.Many2one('project.model')


class ProjectTask(models.Model):
    _name = 'project.tasks'
    _description = 'ProjectTask'

    name = fields.Char(string='Task Name', required=True)
    stage_id = fields.Many2one('project.stages', string='Stage', inverse_name='tasks')
    subtasks = fields.One2many('project.tasks', 'parent_task_id', string='Subtasks')
    parent_task_id = fields.Many2one('project.tasks', string='Parent Task')
    equipment_ids = fields.Many2many('equipment.info', string='Equipment')

