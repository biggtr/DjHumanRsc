from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Create your views here.


def SignupView(request):
    form = None
    # if request.user.is_authenticated:
    #     return HttpResponseForbidden("You've Already Logged in..")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("hr-home")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/signup.html", context={"form": form})
