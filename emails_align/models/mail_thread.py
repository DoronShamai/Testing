# -*- coding: utf-8 -*-
# from odoo import _,fields, models, api
from odoo import _, api, exceptions, fields, models

import email
import email.policy
from email.message import EmailMessage
from email import message_from_string, policy
from odoo.addons.mail.models.mail_thread import MailThread as MailThread


class MailThread(models.AbstractModel):
    _inherit = "mail.thread"

    @api.model
    def _notify_prepare_template_context(self, message, msg_vals, model_description=False, mail_auto_delete=True):

        res = super(MailThread, self)._notify_prepare_template_context(message, msg_vals, model_description=False, mail_auto_delete=True)

        if res["lang"] == 'he_IL':
            res["message"].body = "<div dir='rtl'>" + res["message"].body + "</div>"
       
        return res

   