# abac.py
from policies import get_policy

def check_access(user_attributes, resource_attributes, environment_attributes):
    policy = get_policy(resource_attributes['Type'], user_attributes['Role'])

    if 'access' in policy and policy['access']:
        return True  # Unrestricted access for certain roles, e.g., Admin

    # Adjustments to handle absence of 'allowed_departments' and specificity of 'access_location'
    department_check = user_attributes.get('Department', 'None') in policy.get('allowed_departments', [user_attributes.get('Department', 'None')])
    sensitivity_check = resource_attributes.get('Sensitivity') in policy.get('sensitivity', ['Private'])  # Default to private if not specified
    access_location_check = environment_attributes.get('AccessLocation') in policy.get('access_location', ['OnCampus'])  # Default to on-campus

    return department_check and sensitivity_check and access_location_check
