from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method =="POST":
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("We are happy to have you as our customer"))
            return redirect('login')
    else:
        register_form = UserCreationForm()
    return render(request, 'register.html',{'register_form':register_form})