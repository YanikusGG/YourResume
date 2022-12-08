from django.forms import ModelForm
from polls.models import Resume


# Create the form class.
class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_name', 'name', 'surname', 'age', 'phone', 'email', 'about_education', 'about_work_expirience', 'about_me']
