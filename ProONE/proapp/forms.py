from django import forms
from .models import ProData

# iterable
College = (
    ('', 'Select Your College'),
    ("BCE", "Bhagalpur College of Engineering (BCE)"),
    ("MIT", "Muzaffarpur Institute of Technology (MIT)"),
    ("DCE", "Darbhanga College of Engineering (DCE)"),
    ("MCE", "Motihari College of Engineering (MCE)"),
    ("NCE", "Nalanda College of Engineering (NCE)"),
    ("GCE", "Gaya College of Engineering (GCE)"),
    ("PCE", "Purnea College of Engineering (PCE)"),
    ("BKCE", "Bakhtiyarpur College of Engineering (BKCE)"),
    ("SCE", "Saharsa College of Engineering (SCE)"),
    ("Other", "Other"),
)
Branch=(
    ('','Select Your Branch'),
    ("CSE","Computer Science Engineering"),
    ("ECE","Electronics and Communication Engineering"),
    ("CE","Civil Engineering"),
    ("ME","Mechanical Engineering"),
    ("EE","Electrical Engineering"),
    ("ITE","Information Technology Engineering"),
)

# creating a form
class RegistrationForm(forms.Form):
    name = forms.CharField(
        label='Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Name'
            }
        )
    )
    rollno = forms.CharField(
        label='Roll No.',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Roll No.'
            }
        )
    )
    regno = forms.CharField(
        label='Reg. No.',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Registration No.'
            }
        )
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' Enter Your Email'
            }
        )
    )
    college = forms.ChoiceField(
        choices=College,
        label = 'College',
        widget = forms.widgets.Select(
        attrs={
            'class': 'form-control',
            'placeholder': ' Select Your College'
              }
        )
    )
    branch = forms.ChoiceField(
        choices=Branch,
        label = 'Branch',
        widget = forms.widgets.Select(
        attrs={
            'class': 'form-control',
            'placeholder': ' Select Your Branch'
              }
        )
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name)<=3 or len(name)>=30:
            raise forms.ValidationError("Name Must Have more than 3 or less than 30 Characters ")
        return name

    def clean_rollno(self):
        rollno = self.cleaned_data.get('rollno')
        if len(rollno)<5 or len(rollno)>10:
            raise forms.ValidationError("Roll No. atleast have 5 digits and not more than 10")
        return rollno

    def clean_regno(self):
        regno = self.cleaned_data.get('regno')
        qs = ProData.objects.filter(regno=regno)
        if qs.exists():
            raise forms.ValidationError("It is already registered!")
        elif len(regno)<11 or len(regno)>11 :
            raise  forms.ValidationError("Registration No. Must have 11 digits")
        return regno


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = ProData.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email name is taken already.")
        elif not 'gmail.com' in email:
            raise forms.ValidationError("Email has to end with gmail.com")
        return email

class UpdationForm(forms.Form):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
