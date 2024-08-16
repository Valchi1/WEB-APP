from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Course, Enrollment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'courses/course_form.html'
    fields = ['title', 'description', 'start_date', 'end_date', 'syllabus']

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/course_form.html'
    fields = ['title', 'description', 'start_date', 'end_date', 'syllabus']

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

class EnrollView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=kwargs['pk'])
        Enrollment.objects.get_or_create(
            user=request.user,
            course=course,
        )
        messages.success(request, f'You have been enrolled in {course.title}!')
        return redirect('course_detail', pk=course.pk)

def home(request):
    courses = Course.objects.all()
    return render(request, 'courses/home.html', {'courses': courses})

def user_enrollments(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'courses/user_enrollments.html', {'enrollments': enrollments})
