import re

from django.contrib.auth.backends import ModelBackend

# 自定义用户认证后端
from apps.user.models import UserInfo


class CustomModelBackend(ModelBackend):
    @staticmethod
    def get_user_(account):
        result = re.search(r'^(13\d|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18\d|19[0-35-9])\d{8}$', account)
        if not result:
            result = re.search(r'^[a-zA-Z]\w{4,15}$', account)
            if not result:
                return None
            else:
                user = UserInfo.objects.get(username=account)
                return user
        else:
            user = UserInfo.objects.get(mobile=account)
            return user
