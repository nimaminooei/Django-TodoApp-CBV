from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .form import CustomUserCreationForm


# Create your views here.
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("index")

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("index")
        return super(SignupView, self).get(*args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)

class loginView(LoginView):
    template_name = "accounts/login.html"
    fields = "username", "password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("index")
