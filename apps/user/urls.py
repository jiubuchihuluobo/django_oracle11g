from django.conf.urls import url

from apps.user import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^name/(?P<username>[a-zA-Z]\w{4,15})/$', views.DuplicateUsernameView.as_view()),
    url(r'^mobile/(?P<mobile>(13\d|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18\d|19[0-35-9])\d{8})/$', views.DuplicateMobileView.as_view()),
    url(r'^register/$', views.RegisterView.as_view()),
]
