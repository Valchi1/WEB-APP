from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_superuser or user.groups.filter(name='Administrator').exists():
            context['courses'] = Course.objects.all()
            context['role'] = 'Admin'
        elif user.groups.filter(name='Academic staff').exists():
            context['courses'] = Course.objects.filter(teacher=user)
            context['role'] = 'Teacher'
        elif user.groups.filter(name='Students').exists():
            # Correctly filter courses based on the student's enrollments
            context['courses'] = Course.objects.filter(enrolled_students__student=user)
            context['role'] = 'Student'
        return context
