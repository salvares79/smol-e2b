```python
from django.shortcuts import render, redirect
from .models import UserSchema
from .forms import AddUserForm, EditUserForm

def user_management_page(request):
    return render(request, 'user_management_page.html')

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management_page')
    else:
        form = AddUserForm()
    return render(request, 'add_user_form.html', {'form': form})

def edit_user(request, id):
    user = UserSchema.objects.get(id=id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management_page')
    else:
        form = EditUserForm(instance=user)
    return render(request, 'edit_user_form.html', {'form': form})

def delete_user(request, id):
    user = UserSchema.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return render(request, 'success_message.html')
    return render(request, 'delete_user_confirmation.html', {'user': user})

def view_users(request):
    users = UserSchema.objects.all()
    return render(request, 'user_list.html', {'userList': users})

def view_user(request, id):
    user = UserSchema.objects.get(id=id)
    return render(request, 'single_user.html', {'singleUser': user})
```