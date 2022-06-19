from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout


class LoginView(TemplateView):
    template_name = "authentication.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home-docs")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )

        if not user:
            context = {"login_error": True}
            return render(request, self.template_name, context)

        login(request, user)
        return redirect("home-docs")


class LogoutView(TemplateView):
    template_name = "logout.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("user_auth")
        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def post(request, *args, **kwargs):
        if request.POST.get("logout"):
            logout(request)
            return redirect("user_auth")
        return redirect("home-docs")
