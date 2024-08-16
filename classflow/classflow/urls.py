from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from courses.views import (StudentCoursesView, CourseDetailView, CourseCreateView, CourseUpdateView, EnrollmentCreateView, CoursesListView,CourseContentDeleteView,CourseContentUpdateView )
from dashboard.views import DashboardView
from courses.views import course_content_upload ,  view_course_materials
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path , re_path
from two_factor.urls import urlpatterns as tf_urls
from django.shortcuts import redirect
#from .views import CustomTwoFactorLoginView 
from captcha import views as captcha_views
from django.urls import path
from .views import validate_recaptcha

from two_factor.urls import urlpatterns as two_factor_patterns
from django.views.generic import RedirectView
#from .forms import CaptchaAuthenticationForm


 # Set the app_name attribute




urlpatterns = [
    
   
    
   
   path('admin/', admin.site.urls),
 
   #path('', lambda request: redirect('account/login/')),
   path('', include(tf_urls)),
     path('validate_recaptcha/', validate_recaptcha, name='validate_recaptcha'),
    # Update the login URL to use the custom form with CAPTCHA
   # path('account/login/', auth_views.LoginView.as_view(
      #  template_name='core/login.html',
       # authentication_form=CaptchaAuthenticationForm),
      #  name='login'),
    
  #path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
 # path('', include(tf_urls)),

#path('', include('two_factor.urls', namespace='two_factor')),

path('account/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

   path('logout/', auth_views.LogoutView.as_view(next_page='/account/login/'), name='logout'),
   # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   
  
   
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('courses/', StudentCoursesView.as_view(), name='student_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='view_course'),
    path('courses/add/', CourseCreateView.as_view(), name='add_course'),
    path('courses/<int:pk>/edit/', CourseUpdateView.as_view(), name='change_course'),
    path('enrollments/add/', EnrollmentCreateView.as_view(), name='add_enrollment'),
    path('courses/all/', CoursesListView.as_view(), name='all_courses'),  # Assuming CoursesListView exists in views.py
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('courses/<int:course_id>/upload/', course_content_upload, name='course_content_upload'),
    path('courses/<int:course_id>/materials/', view_course_materials, name='view_course_materials'),
    path('content/<int:pk>/delete/', CourseContentDeleteView.as_view(), name='delete_course_content'),
    path('content/<int:pk>/edit/', CourseContentUpdateView.as_view(), name='edit_course_content'),
 #  path('captcha/', include('captcha.urls')),
  #path('validate_captcha/', validate_captcha_ajax, name='validate_captcha'),
  
] 


    




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 