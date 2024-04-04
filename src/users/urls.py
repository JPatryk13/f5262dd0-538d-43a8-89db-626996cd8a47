from django.urls import path

from .views import CreateUserView, CustomAuthToken

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create_user"),
    path("token/", CustomAuthToken.as_view()),
]
