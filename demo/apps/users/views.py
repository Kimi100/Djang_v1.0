from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User

class RegisterUserNameView(APIView):
    """
    注册账号
    get: 检查用户是否注册
    """
    def get(self, request, username):
        try:
            count_code = User.objects.filter(username=username).count()
        except:
            return Response(status=404)
        num = 1
        if count_code:
            num = 0
        content = {
            'code': num,
            'username': username,
        }
        return Response(content)