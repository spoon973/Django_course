# 自定义过滤器
# 过滤器本质就是python的函数

# 1.自定义过滤器需要使用django.template模块里面的 Library 类
from django.template import Library

# 2.生成一个Library类的实例对象
register = Library()

# 3.使用register对象的filter方法
@register.filter
def mod(num):
    '''判断num是否为偶数'''
    return num % 2 == 0

# 重要：自定义的过滤器，至少有一个参数，最多有两个
@register.filter
def mod_val(num, val):
    '''判断num是否能被val整除'''
    return num % val == 0