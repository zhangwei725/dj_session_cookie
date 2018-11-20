import datetime

from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render

# 第一次请求服务器----->返回cookie信息
# 下次来的时候浏览器自动携带cookie信息 ---> 获取cookie信息 -->根据cookie信息返回响应
from dj_session_cookie import settings

"""
设置
更新
删除
获取

作用域
过期时间

"""
num = 0


# 设置通过HttpResponse
# 获取的操作HttpRequest

def cookie1(request):
    response = HttpResponse('设置cookie信息')
    """
    参数说明
    key   键
    value=''  值 默认的空字符串
    max_age=None,  设置过期的时间,整型   单位是秒
    expires=None, 设置过期时间  时间类型  默认设置一年
    path='/',   限制获取cookie的路径
    domain=None,  设置子域名能访问的到cookie信息
    secure=False,   使用https协议的时候需要设置true
    httponly=False  只能通过http协议传输cookie信息  js无法操作cookie
    """
    # 设置cookie信息
    response.set_cookie('k1', 'hehe', max_age=7 * 24 * 60 * 60)
    # 设置国际时间 单位是时间类型
    response.set_cookie('k2', 'hehe', expires=datetime.timedelta(minutes=10))
    response.set_cookie('k3', 'v3', path='/cookie/set/')
    # response.set_cookie('k4', 'v4', domain='.baidu.com')

    return response


"""
安全问题 
数据量比较小
只能存ASC||
"""


def cookie2(request, ):
    # 获取cookie信息 如果key不存在则抛出异常
    # v1 = request.COOKIES['k1']
    # 获取cookie信息  如果key不存在就返回None
    v1 = request.COOKIES.get('k1')
    if not v1:
        settings.NUM += 1
    response = HttpResponse("")
    # name = '空空'.encode()
    response.set_signed_cookie('k4', 'kongkong', salt=settings.SECRET_KEY)

    v = request.get_signed_cookie('k4', salt=settings.SECRET_KEY)

    return response


# session一定要配合cookie
# 当用户第一次发送请求-----> 当view接受到这个请求,涉及一些session的信息操作的时候
# 设置session数据-->响应中自动添加cookie信息 sessionid
# 第二次访问 ---->浏览器自动携带sessionid---->中间件获取到cookie中的sessionid -->默认情况从数据中获取session对象的数据
# ---->将解密的数据绑定在request.session对象------>能在视图函数中能获取到数据


# 存储数据的
# session存在哪里
def session1(request):
    # ===设置操作
    # 如果key存在则覆盖
    # request.session['k1'] = '1'
    # 如果key存在 则不设置
    # request.session.setdefault('k2', 1)
    #     获取操作
    #     如果key不存在就报错
    v = request.session['k1']
    # 不存在就返回默认值
    v = request.session.get('k1', None)
    return HttpResponse('session操作')
