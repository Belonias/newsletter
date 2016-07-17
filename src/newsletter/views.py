from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)

    if request.user.is_authenticated():
        title = "Welcome Back %s" %(request.user)

    context = {
    "title": title,
    "form": form,

    }

    # we need a valid form
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        # we still want the email although we don't have full_name
        if not full_name:
            full_name = "No Name"
        instance.full_name = full_name
        instance.save()
        context = {
        "title": "Thank you"
        }

    return render(request, "home.html", context)
