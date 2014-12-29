from django import forms
from models import Program
from tinymce.widgets import TinyMCE

class LoginForm(forms.Form):
	#Form used to login to the main site
	#This is using Crispy-Forms module
	username = forms.CharField(
		label = "Username: ",
		max_length = 16,
		required = True,
		)
	password = forms.CharField(
		label = "Password: ",
		max_length = 32,
		required = True,
		)

class ProgramForm(forms.ModelForm):
	#Form for Program creation
	#Define custom widgets for fields here
	class Meta:
		model = Program
		widgets = {
			'description': TinyMCE(attrs={'cols':80, 'rows':30}),
            'fcs_commit': forms.DateInput(attrs={'class':'datepicker'}),
            'fcs_current': forms.DateInput(attrs={'class':'datepicker'}),
            'ec': forms.DateInput(attrs={'class':'datepicker'}),
            'cc': forms.DateInput(attrs={'class':'datepicker'}),
        }
        # exclude=['clarity_id']
        # fields = ['program_id', 'Program_name', 'Project_health','created_by']

class UploadFileForm(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.FileField()