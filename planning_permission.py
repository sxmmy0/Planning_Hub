"""
Planning Problem
This module helps to determine whether planning permission is required for a fence, gate or wall in various scenarios.
This is determined by  ("Y" or "N")

The Universal Conditions (MUST BE DONE FIRST):
- Listed building(s) - 2U1
- Article 2(3) Land Removing Permitted - 2U2
- Article 2(4) - 2U3
- Article 4 - Directive removing the permitted development rights - 2U4
- AONB - 2U5
- Works affecting TPO - 2U6

The Non-Universal Conditions:
(2A Columns) These are used only if no universal condition applies.
  They depend on:
    - Structure Type (fence, wall, gate)
    - Location ("adjacent" vs. "not_adjacent")
    - Height Category (using 4 options: "up_to_1m", "above_1m", "up_to_2m", "above_2m")

  For example, for fences:
    - If adjacent: permitted only if height is "up_to_1m"; any height above 1m (whether "above_1m", "up_to_2m", or "above_2m") requires permission.
    - If not adjacent: permitted if height is "up_to_1m", "above_1m", or "up_to_2m"; if "above_2m", permission is required.

  Walls are permitted if their height is not "above_2m".

Other conditions:
  Additional factors override the baseline outcome:
    - PD Rights Removed with Previous Planning: if True, the outcome is forced to "Y".
    - New Build Property Restrictions: for example, a gate on a new build property will require permission.

Design Criteria:
  - Diligence: All combinations (including edge cases) are covered.
  - Readability: Code is modular, with clear function names, inline comments, and logging.
  - Scalability: The logic is split into universal, non-universal, and modifiers for ease of maintenance.

Difficult/Easy Parts:
    - Difficult: Ensuring all combinations of conditions are covered without redundancy.
    - Easy: The basic structure of the problem is straightforward, with clear rules for each condition.
"""
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def check_universal_conditions(
    is_in_universal_category,
    is_listed_building,
    article_2_3,
    article_2_4,
    article_4_directive,
    aonb,
    affects_tpo,
    pd_rights_removed,
    is_new_build_with_restrictions
):
    """
    Check if any universal condition applies.
    """
    logging.info("Checking universal conditions...")
    universal_conditions = [
        is_in_universal_category,
        is_listed_building,
        article_2_3,
        article_2_4,
        article_4_directive,
        aonb,
        affects_tpo,
        pd_rights_removed,
        is_new_build_with_restrictions,
    ]
    if any(universal_conditions):
        logging.info("A universal condition is met. Planning permission required.")
        return True
    logging.info("No universal conditions are met.")
    return False

def check_non_universal_conditions(adjacent_to_highway, faces_listed_building, height_meters):
    """
    Check non-universal conditions based on location and height.
    """
    logging.info("Checking non-universal conditions...")
    if adjacent_to_highway:
        logging.info(f"Adjacent to highway with height {height_meters}m.")
        if height_meters > 1:
            logging.info("Height exceeds 1m. Planning permission required.")
            return True
        logging.info("Height is within permitted limits. No planning permission required.")
        return False

    if faces_listed_building:
        logging.info(f"Faces listed building with height {height_meters}m.")
        if height_meters > 1:
            logging.info("Height exceeds 1m. Planning permission required.")
            return True
        logging.info("Height is within permitted limits. No planning permission required.")
        return False

    if height_meters > 2:
        logging.info(f"Height exceeds 2m ({height_meters}m). Planning permission required.")
        return True

    logging.info("No non-universal conditions require planning permission.")
    return False
def requires_planning_permission(
    is_in_universal_category=False,
    adjacent_to_highway=False,
    faces_listed_building=False,
    height_meters=0,
    is_listed_building=False,
    article_2_3=False,
    article_2_4=False,
    article_4_directive=False,
    aonb=False,
    affects_tpo=False,
    pd_rights_removed=False,
    is_new_build_with_restrictions=False
):
    """
    Determine if planning permission is required.
    """
    logging.info("Starting planning permission check...")
    if check_universal_conditions(
        is_in_universal_category,
        is_listed_building,
        article_2_3,
        article_2_4,
        article_4_directive,
        aonb,
        affects_tpo,
        pd_rights_removed,
        is_new_build_with_restrictions
    ):
        return "Y"

    if check_non_universal_conditions(adjacent_to_highway, faces_listed_building, height_meters):
        return "Y"

    logging.info("No conditions require planning permission. Returning 'N'.")
    return "N"
