"""
This script is used to test the functionality of the `user_input_planning_permission.py` file.
"""
import unittest
from user_input_planning_permission import requires_planning_permission

class TestPlanningPermission(unittest.TestCase):
    def test_universal_category(self):
        self.assertEqual(requires_planning_permission(is_in_universal_category=True), "Y")

    def test_adjacent_highway_below_1m(self):
        self.assertEqual(requires_planning_permission(adjacent_to_highway=True, height_meters=0.9), "N")

    def test_adjacent_highway_above_1m(self):
        self.assertEqual(requires_planning_permission(adjacent_to_highway=True, height_meters=1.5), "Y")

    def test_faces_listed_building_above_1m(self):
        self.assertEqual(requires_planning_permission(faces_listed_building=True, height_meters=1.1), "Y")

    def test_height_above_2m(self):
        self.assertEqual(requires_planning_permission(height_meters=2.5), "Y")

    def test_no_restrictions(self):
        self.assertEqual(requires_planning_permission(height_meters=1.5), "N")

    def test_article_directive(self):
        self.assertEqual(requires_planning_permission(article_4_directive=True), "Y")

    def test_combo_multiple_flags(self):
        self.assertEqual(
            requires_planning_permission(adjacent_to_highway=True, height_meters=2.5),
            "Y"
        )

if __name__ == '__main__':
    unittest.main()