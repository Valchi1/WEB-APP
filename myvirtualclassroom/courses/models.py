# courses/models.py
from django.conf import settings  # Correct import for settings
from django.db import models
from django.contrib.auth import get_user_model  # Recommended way to reference the User model

# If Course model is defined above, no changes needed here

class Enrollment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # This is okay, but below is recommended for clarity and consistency
        on_delete=models.CASCADE, 
        related_name='enrollments'
    )
    course = models.ForeignKey(
        'Course',  # It's good practice to use a string here, especially if models are in the same file
        on_delete=models.CASCADE, 
        related_name='enrollments'
    )
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevents duplicate enrollments

    def __str__(self):
        return f"{self.user} enrolled in {self.course}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    syllabus = models.URLField(blank=True)  # Assuming you're using an external URL for the syllabus
    # You can add more fields as per your requirement

    def __str__(self):
        return self.title


#model for enrollment 

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevents duplicate enrollments

    def __str__(self):
        return f"{self.user} enrolled in {self.course}"