import re


class RegexTool(object):

    @staticmethod
    def re_mobile(mobile):
        re_mobile_obj = re.compile(r'^(13\d|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18\d|19[0-35-9])\d{8}$')
        result = re_mobile_obj.search(mobile)
        if result is not None:
            return result
        else:
            return None

    @staticmethod
    def re_username(username):
        re_username_obj = re.compile(r'^[a-zA-Z]\w{4,15}$')
        result = re_username_obj.search(username)
        if result is not None:
            return result
        else:
            return None

    @staticmethod
    def re_password(password):
        print(password)
        re_password_obj = re.compile(r'.{8,16}$')
        result = re_password_obj.search(password)
        if result is not None:
            return result
        else:
            return None
