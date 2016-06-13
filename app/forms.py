"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class BootstrapCurveFittingForm(forms.Form):
    """Fitting form for T1, T2  which uses boostrap CSS."""
    t_value = forms.CharField(label='t_value', max_length=254,widget=forms.TextInput(attrs={'size':'100'}))
    y_value = forms.CharField(label='y_value',max_length=254,widget=forms.TextInput(attrs={'size':'100'}))



"""
aha17 input space
""" 
class AHAForm(forms.Form):
   
    t_value = forms.CharField(label='AHA17', max_length=254,widget=forms.TextInput(attrs={'size':'100'}))


class T2Form(forms.Form):
   
    t_value = forms.CharField(label='T2_t', max_length=254,widget=forms.TextInput(attrs={'size':'100'}))
    y_value = forms.CharField(label='T2_y', max_length=254,widget=forms.TextInput(attrs={'size':'100'}))
	
"""
perfusion input space
""" 

class perfusionForm(forms.Form):
   
    t_value = forms.CharField(label='t_value', max_length=254,widget=forms.TextInput(attrs={'size':'100'}))
    y_value = forms.CharField(label='y_value', max_length=254,widget=forms.TextInput(attrs={'size':'100'}))

"""
fcmat input space
""" 
class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    