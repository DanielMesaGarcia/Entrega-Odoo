# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ssg(models.Model):
#     _name = 'ssg.ssg'
#     _description = 'ssg.ssg'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


# models.py

from odoo import models, fields, api

class EmpresaContratadora(models.Model):
    _name = 'ssg.empresa_contratadora'
    _description = 'Empresas contratadoras que encargan proyectos'

    name = fields.Char(string='Nombre de la Empresa', required=True)
    proyectos_contratados = fields.One2many('ssg.proyecto', 'empresa_contratadora_id', string='Proyectos Contratados')

class Proyecto(models.Model):
    _name = 'ssg.proyecto'
    _description = 'Proyectos de desarrollo de software'

    name = fields.Char(string='Nombre del Proyecto', required=True)
    empresa_contratadora_id = fields.Many2one('ssg.empresa_contratadora', string='Empresa Contratadora')
    jefe_proyecto_id = fields.Many2one('res.users', string='Jefe de Proyecto')
    analistas_ids = fields.Many2many('res.users', string='Analistas Asignados')
    tareas_ids = fields.One2many('ssg.tarea', 'proyecto_id', string='Tareas del Proyecto')
    state = fields.Selection([
        ('analisis', 'En Análisis'),
        ('desarrollo', 'En Desarrollo'),
        ('finalizado', 'Finalizado'),
    ], default='analisis', string='Estado del Proyecto')

class Tarea(models.Model):
    _name = 'ssg.tarea'
    _description = 'Tareas dentro de los proyectos'

    name = fields.Char(string='Nombre de la Tarea', required=True)
    proyecto_id = fields.Many2one('ssg.proyecto', string='Proyecto')
    programador_ids = fields.Many2one('res.users', string='Programador Asignado')
    subtareas_ids = fields.One2many('ssg.subtarea', 'tarea_id', string='Subtareas de la Tarea')
    groups = 'ssg.group_programador'
    total_subtareas = fields.Integer(string='Total de Subtareas', compute='_compute_total_subtareas', store=True)

    @api.depends('subtareas_ids')
    def _compute_total_subtareas(self):
        for tarea in self:
            tarea.total_subtareas = len(tarea.subtareas_ids)


class Subtarea(models.Model):
    _name = 'ssg.subtarea'
    _description = 'Subtareas de las tareas'

    name = fields.Char(string='Nombre de la Subtarea', required=True)
    tarea_id = fields.Many2one('ssg.tarea', string='Tarea')

class MiProyectoTask(models.Model):
    _inherit = 'project.task'

    custom_field = fields.Char(string='custom_field')
