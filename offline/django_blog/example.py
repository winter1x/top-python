from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == 'GET':
        return render(
            request,
            "login_page.html",
            context={
                "username": request.GET.get("username"),
            }
        )
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        check_password(username, password)
        ...

from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, world!")

urlpatterns = [
    ...
    path("", IndexView.as_view()),
    ...
]

from django.views.generic.base import TemplateView

urlpatterns = [
    ...
    path("", TemplateView.as_view(template_name="index.html")),
    ...
]

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context