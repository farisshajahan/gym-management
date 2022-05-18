from django.urls import path
from main.router import router
from main.views import SignUpView

urlpatterns = [path("auth/signup/", SignUpView.as_view())]
urlpatterns += router.urls
