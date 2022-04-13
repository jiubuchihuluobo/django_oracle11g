from django.http import JsonResponse
from django.views import View


class LoginView(View):
    def get(self, request):
        return JsonResponse({'errmsg': '错误信息'})


class RegisterView(View):
    def post(self, request):
        return JsonResponse({'errmsg': '错误信息'})


class DuplicateUsernameView(View):
    def get(self):
        return JsonResponse({'errmsg': '错误信息'})
