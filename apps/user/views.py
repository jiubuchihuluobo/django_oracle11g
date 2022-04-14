from django.http import JsonResponse
from django.views import View

from apps.user.models import UserInfo


class LoginView(View):
    def get(self, request):
        return JsonResponse({'errmsg': '错误信息'})


class RegisterView(View):
    def post(self, request):
        return JsonResponse({'errmsg': '错误信息'})


class DuplicateUsernameView(View):
    def get(self, request, username):
        count = UserInfo.objects.filter(username=username).count()
        if count == 0:
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'success', 'errmsg': '用户名重复'})


class DuplicateMobileView(View):
    def get(self, request, mobile):
        count = UserInfo.objects.filter(mobile=mobile).count()
        if count == 0:
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'success', 'errmsg': '手机号重复'})
