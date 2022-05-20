from django.urls import path

from main.router import router
from main.views import LogoutView, SignUpView

urlpatterns = [
    path("user/signup/", SignUpView.as_view()),
    path("logout/", LogoutView.as_view()),
]
urlpatterns += router.urls
