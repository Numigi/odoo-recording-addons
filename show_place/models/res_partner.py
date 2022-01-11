# © 2019 - today Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    type = fields.Selection(selection_add=[("show_site", "Show Site")])
    show_place_type_id = fields.Many2one(
        "show.place.type", string="Show Place Type", prefetch=False
    )
    show_place_configuration_id = fields.Many2one(
        "show.place.configuration",
        string="Show Place Configuration",
        ondelete="restrict",
        prefetch=False,
    )
    show_place_maximum_capacity = fields.Integer(
        string="Show Place Maximum capacity", prefetch=False
    )
    show_place_notes = fields.Text(string="Show Place Notes", prefetch=False)
    show_place_minor_restriction = fields.Boolean(
        string="Show Place Minor Restriction",
        help="Check this box if this place has a restriction for minors.",
        prefetch=False,
    )
    show_place_distance_from_productor = fields.Integer(
        string="Distance from Productor", prefetch=False
    )
    show_place_stage = fields.Selection(
        [("indoor", "Indoor"), ("outdoor", "Outdoor")], prefetch=False
    )
    diffuser_ids = fields.One2many(
        "res.partner.diffuser", "inverse_partner_id", string="Diffuser's Contacts"
    )
