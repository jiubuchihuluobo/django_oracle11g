from django.conf.urls import url

from apps.user import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^username/$', views.LoginView.as_view())

]
