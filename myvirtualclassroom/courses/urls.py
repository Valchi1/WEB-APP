from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    EnrollView,  # Class-based view for enrollment
   
)

urlpatterns = [
    path('', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/new/', CourseCreateView.as_view(), name='course_create'),
    path('course/<int:pk>/edit/', CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('enroll/<int:pk>/', EnrollView.as_view(), name='enroll_course'),  # Updated to use class-based view
     path('my-enrollments/',  EnrollView.as_view(), name='user_enrollments'),
]

