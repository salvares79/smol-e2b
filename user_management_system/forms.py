```python
from django import forms
from .models import UserSchema

class AddUserForm(forms.ModelForm):
    class Meta:
        model = UserSchema
        fields = ['username', 'email', 'first_name', 'last_name']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserSchema
        fields = ['username', 'email', 'first_name', 'last_name']
```