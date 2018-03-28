# -*- coding: utf-8 -*-
# © 2018 Ingetive - <info@ingetive.com>

import logging
import boto3

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class Partner(models.Model):
    _inherit = "res.partner"

    @api.model
    @api.returns('self', lambda rec: rec.id)
    def create(self, vals):
        res = super(Partner, self).create(vals)

        access_key_id = "AKIAJL7YPMKZ2LEZ6MRQ"
        secret_key = "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"
        bucket_name = 'alfa10'
        filename = 'file.txt'

        session = boto3.Session(access_key_id, secret_key)
        s3 = session.resource('s3')

        some_binary_data = b'Here we have some data'
        object2 = s3.Object(bucket_name, filename)
        object2.put(Body=some_binary_data)

        return res
