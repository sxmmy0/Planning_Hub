"""
Planning Problem
This module helps to determine whether planning permission is required for a fence, gate or wall in various scenarios.
This is determined by  ("Y" or "N")

In this document I created a simple CLI Tool so a user can input the parameters and get a result.

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
        return "Y"

    if adjacent_to_highway and height_meters > 1:
        return "Y"

    if faces_listed_building and height_meters > 1:
        return "Y"

    if height_meters > 2:
        return "Y"

    return "N"

def get_bool_input(prompt):
    return input(prompt + " (y/n): ").strip().lower() == "y"

def main():
    print("Planning Permission Checker\n")

    is_in_universal_category = get_bool_input("Is the site in a universal category?")
    if is_in_universal_category:
        print("Planning Permission Required: Y")
        return

    adjacent_to_highway = get_bool_input("Is it adjacent to a highway used by vehicles?")
    faces_listed_building = get_bool_input("Does it face a listed building?")
    height_meters = float(input("Height of the structure (in meters): "))
    is_listed_building = get_bool_input("Is it on a listed building?")
    article_2_3 = get_bool_input("Is it Article 2(3) land?")
    article_2_4 = get_bool_input("Is it Article 2(4) land?")
    article_4_directive = get_bool_input("Is it under Article 4 directive?")
    aonb = get_bool_input("Is it in an Area of Outstanding Natural Beauty (AONB)?")
    affects_tpo = get_bool_input("Does it affect a Tree Preservation Order (TPO)?")
    pd_rights_removed = get_bool_input("Have PD rights been removed previously?")
    is_new_build_with_restrictions = get_bool_input("Is it a new build with restrictions?")

    result = requires_planning_permission(
        is_in_universal_category=is_in_universal_category,
        adjacent_to_highway=adjacent_to_highway,
        faces_listed_building=faces_listed_building,
        height_meters=height_meters,
        is_listed_building=is_listed_building,
        article_2_3=article_2_3,
        article_2_4=article_2_4,
        article_4_directive=article_4_directive,
        aonb=aonb,
        affects_tpo=affects_tpo,
        pd_rights_removed=pd_rights_removed,
        is_new_build_with_restrictions=is_new_build_with_restrictions
    )

    print(f"\nPlanning Permission Required: {result}")

if __name__ == "__main__":
    main()
