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
    # 1. Check universal categories first
    if (
        is_in_universal_category or
        is_listed_building or
        article_2_3 or
        article_2_4 or
        article_4_directive or
        aonb or
        affects_tpo or
        pd_rights_removed or
        is_new_build_with_restrictions
    ):
        return "Y"  # Planning permission required

    # 2. Check specific conditions
    if adjacent_to_highway:
        if height_meters > 1:
            return "Y"
        else:
            return "N"

    if faces_listed_building:
        if height_meters > 1:
            return "Y"
        else:
            return "N"

    if height_meters > 2:
        return "Y"

    return "N"  # If none of the conditions apply

# Example 1: On Article 4 Land
requires_planning_permission(article_4_directive=True)
# ➜ "Y"

# Example 2: Next to a highway, 0.8m high
requires_planning_permission(adjacent_to_highway=True, height_meters=0.8)
# ➜ "N"

# Example 3: Next to a highway, 1.2m high
requires_planning_permission(adjacent_to_highway=True, height_meters=1.2)
# ➜ "Y"
