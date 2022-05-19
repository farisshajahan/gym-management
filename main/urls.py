from django.urls import path

from main.router import router
from main.views import SignUpView

urlpatterns = [path("user/signup/", SignUpView.as_view())]
urlpatterns += router.urls
