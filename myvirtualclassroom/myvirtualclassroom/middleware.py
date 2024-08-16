# myvirtualclassroom/middleware.py

#class ABACMiddleware:
  #  def __init__(self, get_response):
       # self.get_response = get_response

    #def __call__(self, request):
        # Your custom logic here
        
        # Continue processing the request
       # return self.get_response(request)
       
       # middleware.py (in your main Django app)
import logging
from django.http import HttpResponseForbidden
from authentication.abac import check_access

# Configure logging
logger = logging.getLogger(__name__)

# Define your on-campus IP range
ON_CAMPUS_IP_RANGE = ['192.168.1.1']  # Adjust as necessary for your use case

class ABACMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if request.path.startswith('/admin'):
           return self.get_response(request)
        
        # Log the start of the ABAC check
        logger.debug('Starting ABAC check for user: %s', request.user)

        # Assume user has no role if not in any groups
        user_role = request.user.groups.first().name if request.user.groups.exists() else 'NoRole'

        user_attributes = {
            'Role': user_role,
            # Potentially add other user attributes here
        }

        # Initialize resource_attributes with a placeholder
        resource_attributes = {
            'Type': 'Unknown',  # Default value if we can't determine the type
        }

        # Check if request.resolver_match is not None before accessing attributes
        if request.resolver_match:
            resource_attributes['Type'] = request.resolver_match.app_name if request.resolver_match.app_name else 'Unknown'

        environment_attributes = {
            'AccessLocation': 'OnCampus' if any(addr in request.META['REMOTE_ADDR'] for addr in ON_CAMPUS_IP_RANGE) else 'OffCampus',
            # Potentially add other environment attributes here
        }
        
        # Guard for unauthenticated access to protected views
        if not request.user.is_authenticated and not getattr(request.resolver_match.func, 'public_access', False) if request.resolver_match else True:
            logger.warning('Forbidden: Unauthenticated access attempt to a protected view by %s.', request.user)
            return HttpResponseForbidden()

        # Perform the ABAC check
        if not check_access(user_attributes, resource_attributes, environment_attributes):
            logger.warning('Forbidden: User %s does not have ABAC access rights for %s.', request.user, resource_attributes['Type'])
            return HttpResponseForbidden()

        # Log the successful ABAC check
        logger.debug('ABAC check passed for user: %s accessing %s', request.user, resource_attributes['Type'])

        response = self.get_response(request)
        return response

