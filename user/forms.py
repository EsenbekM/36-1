from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Passwords do not match')
        
        # if len(password) < 8:
        #     raise forms.ValidationError('Password is too short')
        
        # if len(password) > 50:
        #     raise forms.ValidationError('Password is too long')
        
        # if password.isdigit():
        #     raise forms.ValidationError('Password must contain letters')
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput)


class VeryfyForm(forms.Form):
    code = forms.CharField(max_length=5, required=True)


class ProfileForm(forms.Form): # User, Profile
    username = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
