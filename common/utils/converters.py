class MobileConverter(object):
    """自定义路由转换器去匹配手机号"""
    # 定义匹配手机号的正则表达式
    regex = r'^(13\d|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18\d|19[0-35-9])\d{8}$'

    def to_python(self, value):
        # to_python:将匹配结果传递到视图内部时使用
        return str(value)

    def to_url(self, value):
        # to_url:将匹配结果用于url反向解析传值时使用
        return str(value)


class UsernameConverter(object):
    """自定义路由转换器去匹配用户名"""
    # 定义匹配用户名的正则表达式
    regex = r'^[a-zA-Z][a-zA-Z0-9_]{4,15}$'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return str(value)
