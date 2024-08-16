# policies.py
from attributes import DEPARTMENTS, RESOURCE_TYPES, SENSITIVITY_LEVELS, ACCESS_LOCATIONS

policies = {
    'Lecture_Videos': {
        'Professor': {
            'allowed_departments': DEPARTMENTS,
            'sensitivity': ['Public', 'Private'],
            'access_location': ACCESS_LOCATIONS,
        },
        'Student': {
            'sensitivity': ['Public'],
            'access_location': ACCESS_LOCATIONS,
        },
        'Guest': {
            'sensitivity': ['Public'],
            'access_location': ACCESS_LOCATIONS,  # Guests can access public lecture videos from any location
        },
    },
    'Assignments': {
        'Professor': {
            'allowed_departments': DEPARTMENTS,
            'sensitivity': ['Private'],
            'access_location': ACCESS_LOCATIONS,
        },
        'Student': {
            'sensitivity': ['Public', 'Private'],  # Assuming students can access both public and private assignments
            'access_location': ['OnCampus'],  # But private assignments can only be accessed on campus
        },
        'IT_Staff': {
            'sensitivity': ['Private'],  # IT_Staff has specific restrictions, assumed for the example
            'access_location': ['OnCampus'],  # They can access private assignments but only on campus
        },
        'Guest': {
            'sensitivity': ['Public'],  # Guests can only access public assignments
            'access_location': ACCESS_LOCATIONS,  # No restriction on location for public assignments
        },
    },
    'Grades_Report': {
        # Your existing definitions...
    },
    'Course_Materials': {
        # Your existing definitions...
    },
}

def get_policy(resource_type, user_role):
    return policies.get(resource_type, {}).get(user_role, {})
