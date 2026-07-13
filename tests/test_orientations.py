import sys
from types import ModuleType
import unittest


backend = ModuleType("javakh_interface")
backend.calls = []


def solve_signed_variants(pd_code, signs):
    backend.calls.append((pd_code, signs))
    return [str(row) for row in signs] + ([str(signs[0])] if signs else [])


backend.solve_signed_variants = solve_signed_variants
sys.modules["javakh_interface"] = backend

from link_khovanov import link_khovanov


TREFOIL = [[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]]
HOPF = [[2, 3, 1, 4], [4, 1, 3, 2]]


class OrientationTests(unittest.TestCase):
    def setUp(self):
        backend.calls.clear()

    def test_knot_has_one_sign_variant_and_results_are_deduplicated(self):
        result = link_khovanov(TREFOIL)
        self.assertEqual(len(backend.calls), 1)
        _, rows = backend.calls[0]
        self.assertEqual(len(rows), 1)
        self.assertEqual(len(rows[0]), 3)
        self.assertEqual(result, [str(rows[0])])

    def test_hopf_link_has_two_global_orientation_classes(self):
        link_khovanov(HOPF)
        _, rows = backend.calls[0]
        self.assertEqual(len(rows), 2)
        self.assertEqual(len({tuple(row) for row in rows}), 2)
        self.assertTrue(all(set(row) <= {-1, 1} for row in rows))

    def test_sign_equivalent_split_orientations_are_submitted_once(self):
        split = [[1, 1, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6]]
        link_khovanov(split)
        _, rows = backend.calls[0]
        self.assertEqual(len(rows), 1)

    def test_invalid_pd_code_is_rejected_before_backend(self):
        with self.assertRaisesRegex(ValueError, "invalid PD"):
            link_khovanov([[1, 2, 3, 4]])
        self.assertEqual(backend.calls, [])


if __name__ == "__main__":
    unittest.main()
