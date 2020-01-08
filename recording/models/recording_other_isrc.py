# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class RecordingOtherISRC(models.Model):

    _name = 'recording.other.isrc'
    _description = 'Recording Other ISRC'
    _order = 'sequence'

    recording_id = fields.Many2one(
        'recording',
        ondelete='cascade',
        required=True,
    )
    sequence = fields.Integer()
    isrc = fields.Char('ISRC', size=12, required=True)
    partner_id = fields.Many2one(
        'res.partner', 'Issuer',
        required=True,
    )
    notes = fields.Text()