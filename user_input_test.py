import unittest
from planning_permission import (
    requires_planning_permission,
    check_universal_conditions,
    check_non_universal_conditions,
)

class TestPlanningPermission(unittest.TestCase):
    def test_universal_conditions(self):
        self.assertTrue(check_universal_conditions(
            is_in_universal_category=True,
            is_listed_building=False,
            article_2_3=False,
            article_2_4=False,
            article_4_directive=False,
            aonb=False,
            affects_tpo=False,
            pd_rights_removed=False,
            is_new_build_with_restrictions=False
        ))

    def test_non_universal_conditions_adjacent_highway(self):
        self.assertTrue(check_non_universal_conditions(
            adjacent_to_highway=True,
            faces_listed_building=False,
            height_meters=1.5
        ))

    def test_non_universal_conditions_faces_listed_building(self):
        self.assertTrue(check_non_universal_conditions(
            adjacent_to_highway=False,
            faces_listed_building=True,
            height_meters=1.2
        ))

    def test_requires_planning_permission_universal(self):
        self.assertEqual(requires_planning_permission(is_in_universal_category=True), "Y")

    def test_requires_planning_permission_non_universal(self):
        self.assertEqual(requires_planning_permission(adjacent_to_highway=True, height_meters=1.5), "Y")

    def test_requires_planning_permission_no_conditions(self):
        self.assertEqual(requires_planning_permission(height_meters=1.0), "N")

if __name__ == '__main__':
    unittest.main()