# -*- coding: utf-8 -*-

import math

from odoo import models, fields, api, _
from odoo.tools import amount_to_text_en, float_round
from odoo.exceptions import UserError, ValidationError

from odoo.addons.amount_to_word_base.models.amount_to_text_en import amount_to_text_en
from odoo.addons.amount_to_word_base.models.amount_to_text_ar import amount_to_text_ar, ennotoarno

class AccountPayment(models.Model):
    _inherit = "account.payment"


    def get_partner_lang(self):
	currency_lang = 'english'
	if self.partner_id and self.partner_id.lang:
	    lang_ids = self.env['res.lang'].search([('code', '=', self.partner_id.lang)])
	    for lang in lang_ids:
		currency_lang = lang.currency_lang
        return currency_lang

    def amount_to_text(self, amount, currency_id):
	partner_lang = self.get_partner_lang()
	if partner_lang == 'arabic':
	    return amount_to_text_ar(amount, currency=currency_id)
        return amount_to_text_en(amount, currency=currency_id)



    def ennotoarno(self, amount):
        return ennotoarno(amount)


