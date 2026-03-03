from odoo.tests.common import TransactionCase


class TestWaveGrouping(TransactionCase):
    def test_empty(self):
        self.assertEqual(self.env["stock.picking"].group_pickings_for_wave([]), [])
