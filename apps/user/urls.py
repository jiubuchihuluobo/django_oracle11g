from django.conf.urls import url

from apps.user import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^(?P<username>[a-zA-Z][a-zA-Z0-9_]{4,15})/$', views.DuplicateUsernameView.as_view()),
    url(r'^(?P<mobile>(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8})/$', views.DuplicateMobileView.as_view()),
    # url(r'', views.RegisterView.as_view())
]
