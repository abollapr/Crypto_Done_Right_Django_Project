from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from Landing_page.forms import RegistrationForm
from django.contrib.auth.models import User
from .models import Landing_page_template
# Create your views here.
def home(request):
    return render(request, 'landing_page.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Landing_page')
    else:
        form = RegistrationForm()

        args = {'form': form }
        return render(request, 'reg_form.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)

def landing_page(request):
    if request.method == 'POST':
        title = request.POST
        new_landing_page = Landing_page_template(heading= title['heading'], introduction="This is the beginning!")
        new_landing_page.save()
    else:
        return render(request, 'landing_page_form.html')

def preview_landing_page(request):
    QuerySet_Dict = {}
    for e in Landing_page_template.objects.all():
        QuerySet_Dict['heading'] = e.heading
    return render(request, 'landing_page.html', QuerySet_Dict)
