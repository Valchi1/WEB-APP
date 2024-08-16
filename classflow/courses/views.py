from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment
from classflow.forms import CourseForm, EnrollmentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import CourseContentForm
from django.urls import reverse
from django.views.generic import DeleteView
from .models import CourseContent
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required








class StudentCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/student_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(enrollments__student=self.request.user)

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'courses/view_materials.html'
      # Example permission
    # Add the rest of your view definition here...
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include course content in context
        context['materials'] = self.object.content.all()  # Assuming 'content' is the related_name in CourseContent model
        context['is_teacher'] = self.request.user == self.object.teacher or self.request.user.is_superuser
        return context

class CourseCreateView(PermissionRequiredMixin, CreateView):
    form_class = CourseForm
    template_name = 'courses/add_course.html'
    permission_required = 'courses.can_add_course'
    success_url = reverse_lazy('all_courses')

class CourseUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = CourseForm
    template_name = 'courses/change_course.html'
    permission_required = 'courses.can_change_course'
    success_url = reverse_lazy('all_courses')

class EnrollmentCreateView(LoginRequiredMixin, CreateView):
    form_class = EnrollmentForm
    template_name = 'enrollments/add_enrollment.html'
    success_url = reverse_lazy('student_courses')

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)
    
    
    
# views.py
from django.views.generic import ListView
from .models import Course

class CoursesListView(ListView):
    model = Course
    template_name = 'courses/all_courses.html'
    context_object_name = 'courses'  # This is the variable name you will use in your template

    def get_queryset(self):
        # If the user is an admin, return all courses
        if self.request.user.is_superuser:
            return Course.objects.all()
        # Otherwise, return an empty queryset or only courses associated with the user
        return Course.objects.none()  # or filter based on the user's role









#class CoursesListView(PermissionRequiredMixin, ListView):
 #   model = Course
   # template_name = 'courses/all_courses.html'
   # permission_required = 'courses.view_courses'  # Example permission

    #def get_queryset(self):
        # Optional: Customize the queryset if needed, e.g., order by, filtering
       # return super().get_queryset().order_by('title')




@login_required
def course_content_upload(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Check if the user is the teacher of the course or an admin
    if not (request.user == course.teacher or request.user.is_superuser):
        raise PermissionDenied
    
    if request.method == 'POST':
        form = CourseContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.course = course
            content.created_by = request.user
            content.save()
            return redirect(reverse('view_course', kwargs={'pk': course.pk}))
    else:
        form = CourseContentForm()
    return render(request, 'courses/upload_content.html', {'form': form, 'course': course})













#def course_content_upload(request, course_id):
   # course = get_object_or_404(Course, id=course_id, teacher=request.user)
    #if request.method == 'POST':
        #form = CourseContentForm(request.POST, request.FILES)
       # if form.is_valid():
          #  content = form.save(commit=False)
         #   content.course = course
          #  content.created_by = request.user
          #  content.save()
            # Assuming you have a 'course_detail' view to redirect to that shows the course content
           # return redirect(reverse('view_course', kwargs={'pk': course.pk}))
   # else:
       # form = CourseContentForm()
   # return render(request, 'courses/upload_content.html', {'form': form, 'course': course})


# views.py
def view_course_materials(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    materials = course.content.all()
    return render(request, 'courses/view_materials.html', {'course': course, 'materials': materials})



class CourseContentDeleteView(UserPassesTestMixin, DeleteView):
    model = CourseContent
    template_name = 'courses/confirm_delete.html'  # Confirm deletion page
    success_url = reverse_lazy('all_courses')  # Adjust the redirect as needed

    def test_func(self):
        content = self.get_object()
        return self.request.user == content.created_by or self.request.user.is_superuser



class CourseContentDeleteView(UserPassesTestMixin, DeleteView):
    model = CourseContent
    template_name = 'courses/confirm_delete.html'  # Your template for confirming deletion

    def get_success_url(self):
        """
        Redirects to the course detail page of the deleted content's associated course.
        """
        course_id = self.object.course.pk  # Assuming 'course' is the ForeignKey in CourseContent model
        return reverse('view_course', kwargs={'pk': course_id})

    def test_func(self):
        """
        Ensures that only the content creator or an admin can delete the course content.
        """
        content = self.get_object()
        return self.request.user == content.created_by or self.request.user.is_superuser
    
    
    
class CourseContentUpdateView(UserPassesTestMixin, UpdateView):
    model = CourseContent
    form_class = CourseContentForm  # Use the form class you've defined for course content
    template_name = 'courses/edit_course_content.html'  # Your template for updating content

    def get_success_url(self):
        """
        Redirects to the course detail page of the updated content's associated course.
        """
        course_id = self.object.course.pk  # Assuming 'course' is the ForeignKey in CourseContent model
        return reverse('view_course', kwargs={'pk': course_id})

    def test_func(self):
        """
        Ensures that only the content creator or an admin can update the course content.
        """
        content = self.get_object()
        return self.request.user == content.created_by or self.request.user.is_superuser