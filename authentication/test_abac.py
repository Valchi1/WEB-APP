# test_abac.py
import pytest
from abac import check_access

# Existing tests...

def test_professor_access_confidential_course_materials_on_campus():
    assert check_access(
        {'Role': 'Professor', 'Department': 'Faculty_of_Science'},
        {'Type': 'Course_Materials', 'Sensitivity': 'Private'},
        {'AccessLocation': 'OnCampus'}
    )

def test_professor_denied_grades_report_off_campus():
    assert not check_access(
        {'Role': 'Professor', 'Department': 'Faculty_of_Science'},
        {'Type': 'Grades_Report', 'Sensitivity': 'Private'},
        {'AccessLocation': 'OffCampus'}
    )

def test_it_staff_access_grades_report_on_campus():
    assert check_access(
        {'Role': 'IT_Staff', 'Department': 'Faculty_of_Engineering'},
        {'Type': 'Grades_Report', 'Sensitivity': 'Private'},
        {'AccessLocation': 'OnCampus'}
    )

def test_it_staff_denied_assignments_off_campus():
    assert not check_access(
        {'Role': 'IT_Staff', 'Department': 'Faculty_of_Engineering'},
        {'Type': 'Assignments', 'Sensitivity': 'Private'},
        {'AccessLocation': 'OffCampus'}
    )

def test_guest_access_public_lecture_videos_on_campus():
    assert check_access(
        {'Role': 'Guest', 'Department': None},
        {'Type': 'Lecture_Videos', 'Sensitivity': 'Public'},
        {'AccessLocation': 'OnCampus'}
    )

def test_guest_denied_private_assignments_off_campus():
    assert not check_access(
        {'Role': 'Guest', 'Department': None},
        {'Type': 'Assignments', 'Sensitivity': 'Private'},
        {'AccessLocation': 'OffCampus'}
    )

# Running the tests with pytest will validate these scenarios.
