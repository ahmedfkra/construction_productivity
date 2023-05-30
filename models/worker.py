from odoo import fields, models, api


class Worker(models.Model):
    _name = 'project.worker'
    _description = 'Description'

    name = fields.Many2one('res.partner', string='Worker')
    work_hours = fields.Integer(string='Work Hours')
    worker_equ = fields.Many2many('equipment.info', string='Worker Equipment')
    type_worker = fields.Selection([('driver', 'Driver'), ('worker', 'Worker')], string='Worker Type')


class ProductionWorker(models.Model):
    _name = 'worker.production'
    _description = 'Description'
    _rec_name = 'worker_id'

    work_day = fields.Date(string='Work day')
    worker_id = fields.Many2one('project.worker', string='Worker')
    dist = fields.Float(string='Distance')
    equ_id = fields.Many2one('equipment.info', string='Equipment')
    rate_work_achieved = fields.Float('Rate Achieved')
    target_work = fields.Float('Target work')
    actual_work_prod = fields.Float(string='Actual Production')
    deviation = fields.Float(string='Deviation')
    note = fields.Char(string='Note')


class WorkerTask(models.Model):
    _name = 'worker.tasks'

    name = fields.Char(string='Task')
