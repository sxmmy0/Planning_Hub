"""
Planning Problem
This module provides a CLI tool to determine whether planning permission is required for a fence, gate, or wall.
"""

from planning_permission import (
    requires_planning_permission,
    check_universal_conditions,
    check_non_universal_conditions
)

def get_bool_input(prompt):
    """
    Helper function to get a boolean input from the user.
    """
    return input(prompt + " (y/n): ").strip().lower() == "y"

def main():
    """
    Main function to interactively collect user input and determine planning permission.
    """
    print("Planning Permission Checker\n")

    # Collect inputs for universal conditions
    is_in_universal_category = get_bool_input("Is the site in a universal category?")
    is_listed_building = get_bool_input("Is it on a listed building?")
    article_2_3 = get_bool_input("Is it Article 2(3) land?")
    article_2_4 = get_bool_input("Is it Article 2(4) land?")
    article_4_directive = get_bool_input("Is it under Article 4 directive?")
    aonb = get_bool_input("Is it in an Area of Outstanding Natural Beauty (AONB)?")
    affects_tpo = get_bool_input("Does it affect a Tree Preservation Order (TPO)?")
    pd_rights_removed = get_bool_input("Have PD rights been removed previously?")
    is_new_build_with_restrictions = get_bool_input("Is it a new build with restrictions?")

    # Check universal conditions first
    if check_universal_conditions(
        is_in_universal_category=is_in_universal_category,
        is_listed_building=is_listed_building,
        article_2_3=article_2_3,
        article_2_4=article_2_4,
        article_4_directive=article_4_directive,
        aonb=aonb,
        affects_tpo=affects_tpo,
        pd_rights_removed=pd_rights_removed,
        is_new_build_with_restrictions=is_new_build_with_restrictions
    ):
        print("Planning Permission Required: Y")
        return

    # Collect inputs for non-universal conditions
    adjacent_to_highway = get_bool_input("Is it adjacent to a highway used by vehicles?")
    faces_listed_building = get_bool_input("Does it face a listed building?")
    height_meters = float(input("Height of the structure (in meters): "))

    # Check non-universal conditions
    if check_non_universal_conditions(
        adjacent_to_highway=adjacent_to_highway,
        faces_listed_building=faces_listed_building,
        height_meters=height_meters
    ):
        print("Planning Permission Required: Y")
        return

    # If no conditions require planning permission
    print("Planning Permission Required: N")

if __name__ == "__main__":
    main()