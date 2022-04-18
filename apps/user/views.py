import json
import re

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from apps.user.models import UserInfo
from common.utils.regex import RegexTool


class LoginView(View):
    def get(self, request):
        json_dict = json.loads(request.body)
        username = json_dict.get('username')
        password = json_dict.get('password')
        remember = json_dict.get('remember')
        if re.search(r'^(13\d|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18\d|19[0-35-9])\d{8}$', username):
            UserInfo.USERNAME_FIELD = 'mobile'
        elif re.search(r'^[a-zA-Z]\w{4,15}$', username):
            UserInfo.USERNAME_FIELD = 'username'
        else:
            return JsonResponse({'status': 'failure', 'errmsg': '用户名格式错误'})
        user = authenticate(request, username=username, password=password)
        if not user:
            return JsonResponse({'status': 'failure', 'errmsg': '用户密码错误'})
        else:
            login(request=request, user=user)
            if not remember:
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(None)
        return JsonResponse({'status': 'success'})
        # user_obj = UserInfo.objects.filter(username=username).first()
        # result = UserInfo.check_password(self=user_obj, raw_password=password)


class RegisterView(LoginRequiredMixin, View):
    def post(self, request):
        json_dict = json.loads(request.body)
        username = json_dict.get('username')
        password_1 = json_dict.get('password1')
        password_2 = json_dict.get('password2')
        if RegexTool.re_username(username) is None:
            return JsonResponse({'status': 'failure', 'errmsg': '用户名格式错误'})
        if RegexTool.re_password(password_1) is None or password_2 != password_1:
            return JsonResponse({'status': 'failure', 'errmsg': '密码输入不一致或格式错误'})
        UserInfo.objects.create_user(username=username, password=password_2)
        return JsonResponse({'status': 'success'})


class DuplicateUsernameView(View):
    def get(self, request, username):
        count = UserInfo.objects.filter(username=username).count()
        if request.user.is_authenticated is True:
            print('认证成功')
        else:
            print('认证失败')
        if count == 0:
            return JsonResponse({'status': 'success', 'username': username})
        else:
            return JsonResponse({'status': 'failure', 'errmsg': '用户名重复'})


class DuplicateMobileView(View):
    def get(self, request, mobile):
        count = UserInfo.objects.filter(mobile=mobile).count()
        print(request.user.is_authenticated)
        if count == 0:
            return JsonResponse({'status': 'success', 'mobile': mobile})
        else:
            return JsonResponse({'status': 'failure', 'errmsg': '手机号重复'})
