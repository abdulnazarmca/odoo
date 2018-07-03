# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import except_orm, Warning, RedirectWarning, UserError, ValidationError


class Currency(models.Model):
    _inherit = "res.currency"

    name_before_decimal = fields.Char(string='Name Before Decimal', required=True, default='Dirham', translate=True)
    name_after_decimal = fields.Char(string='Name After Decimal', required=True, default='Fil', translate=True)

class Lang(models.Model):
    _inherit = "res.lang"


    currency_lang = fields.Selection([('english', 'English'),('arabic', 'Arabic')], string='Currency Language', default='english')


