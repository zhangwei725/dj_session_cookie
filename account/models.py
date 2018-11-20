from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# 字段 属性
# 方法  行为
#  property  对数据进行计算,校验
# 声明的时候是函数
# 使用的时候字段

# 加密  不可逆
#
class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    _password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'

    #  property
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = make_password(password, 'pbkdf2_sha256')

    def verify_password(self, password):
        return check_password(password, self._password)



