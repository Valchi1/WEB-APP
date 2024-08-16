from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

def list_users(request):
    users = User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})
