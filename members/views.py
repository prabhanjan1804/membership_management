from django.shortcuts import render, redirect
from .forms import RegistrationForm, PassiveRenewalForm
from .models import Member
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, user_passes_test 
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib import messages

def is_director(user):
    return user.groups.filter(name='Vorstand').exists()

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thanks.html")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


@login_required
@user_passes_test(is_director)
def approve_members(request):
    members = Member.objects.filter(status='PENDING')
    if request.method == "POST":
        for m in members:
            if f"approve_{m.id}" in request.POST:
                m.approve()
            elif f"deny_{m.id}" in request.POST:
                m.status = 'DENIED'
                m.save()
    return render(request, "approval_panel.html", {"members": members})

@login_required
def member_list(request):
    if not is_director(request.user):
        raise PermissionDenied  # optional: custom 403 page
    members = Member.objects.all().order_by('name')
    return render(request, 'member_list.html', {'members': members})



def passive_renewal(request):
    if request.method == 'POST':
        form = PassiveRenewalForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.status = 'PASSIVE'
            member.save()
            messages.success(request, "Your passive membership renewal request has been submitted.")
            return redirect('passive_renewal')
    else:
        form = PassiveRenewalForm()

    return render(request, 'passive_renewal.html', {'form': form})

def logout_success(request):
    return render(request, 'registration/logout.html')