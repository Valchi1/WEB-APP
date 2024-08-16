from django import forms
from courses.models import Course, Enrollment










class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
        }
        
        



import requests
from django.http import JsonResponse

def validate_recaptcha(request):
    if request.method == 'POST':
        captcha_response = request.POST.get('g-recaptcha-response')
        if captcha_response:
            # Validate the reCAPTCHA response using Google's reCAPTCHA verification endpoint
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
                'secret': '6LcvQ70pAAAAABqgW9Jr3rXP5DJAWPCRt6bEb0ho',
                'response': captcha_response
            })
            data = response.json()
            if data['success']:
                # Valid reCAPTCHA response
                return JsonResponse({'success': True})
            else:
                # Invalid reCAPTCHA response
                return JsonResponse({'success': False, 'error_message': 'Invalid reCAPTCHA response'})
        else:
            # Missing reCAPTCHA response
            return JsonResponse({'success': False, 'error_message': 'No reCAPTCHA response provided'})
    else:
        # Invalid request method
        return JsonResponse({'success': False, 'error_message': 'Invalid request method'})






