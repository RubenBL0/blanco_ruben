# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cualificacions(models.Model):
    _name = 'blanco_ruben.cualificacions'
    _description = 'Cualificacións dos alumnos'

    apelidos = fields.Char(string='Apelidos')
    nome = fields.Char(string='Nome')
    ano = fields.Char(string='Ano Académico')
    ciclo = fields.Char(string='Ciclo')
    quenda = fields.Selection([('Ordinario','Ordinario'),('Vespertino','Vespertino'),('FPDual','FPDual')], string='Quenda')
    curso = fields.Char(string='Curso')
    modulo = fields.Char(string='Módulo')
    nota = fields.Integer(string='Nota')
    notatexto = fields.Char(compute="_notatexto", string='Nota Texto')


    @api.depends('nota')
    def _notatexto(self):
        for rexistro in self:
            if rexistro.nota < 5:
                rexistro.notatexto = "Suspenso"
            elif rexistro.nota == 5:
                rexistro.notatexto = "Aprobado"
            elif rexistro.nota == 6:
                rexistro.notatexto = "Ben"
            elif rexistro.nota > 6 and rexistro.nota < 9:
                rexistro.notatexto = "Notable"
            else:
                rexistro.notatexto = "Sobresaliente"

