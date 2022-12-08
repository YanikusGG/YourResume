from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from polls.forms import ResumeForm
from polls.models import Resume
import pdfkit

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(user=request.user.id)
    return render(request, 'resume_list.html', locals())

@login_required
def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()
            return redirect('resume_list_url')
        else:
            return render(request, 'create_resume.html', locals())
    form = ResumeForm()
    return render(request, 'create_resume.html', locals())

@login_required
def resume_download(request, resume_name):
    resume = Resume.objects.get(user=request.user.id, resume_name=resume_name)
    pdf = pdfkit.from_string(render_to_string('resume.html', locals(), request), False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="YourResume"'
    return response

@login_required
def resume_view(request, resume_name):
    resume = Resume.objects.get(user=request.user.id, resume_name=resume_name)
    return render(request, 'resume.html', locals())
