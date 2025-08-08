from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('approve')

    def get_success_url(self):
        return self.get_redirect_url() or self.success_url

def logout_view(request):
    logout(request)
    return redirect('logout_success')
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('logout/success/', views.logout_success, name='logout_success'),  
    path('register/', views.register, name='register'),
    path('approve/', views.approve_members, name='approve'),
    path('renew/', views.passive_renew, name='renew'),
    path('members/', views.member_list, name='member_list'),
]