from collections import defaultdict
from odoo import api, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    def group_pickings_for_wave(self, picking_ids, max_lines=60):
        groups = defaultdict(list)
        for picking in self.browse(picking_ids):
            groups[picking.location_id.id].append(picking.id)
        waves = []
        for location_id, ids in groups.items():
            for i in range(0, len(ids), max_lines):
                waves.append({"location_id": location_id, "picking_ids": ids[i : i + max_lines]})
        return waves
