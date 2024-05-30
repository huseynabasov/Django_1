from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="Istifadeci adi")
    password = forms.CharField(max_length=15, label="Sifre", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=15, label="Sifreni tesdiqle", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data["username"]
        password = self.cleaned_data["password"]
        confirm = self.cleaned_data["confirm"]
        
        
        if password and confirm and password != confirm:
            raise forms.ValidationError("Sifreler eyni deil!")
        
        values = {
            "username": username,
            "password": password
        }
        
        return values
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label="Istifadeci adi")
    password = forms.CharField(max_length=15, label="Sifre", widget=forms.PasswordInput) 

  