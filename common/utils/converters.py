class MobileConverter(object):
    """自定义路由转换器去匹配手机号"""
    # 定义匹配手机号的正则表达式
    regex = r'^(13[0-9]|14[5|7]|15[0|1|2|3|4|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$'

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
