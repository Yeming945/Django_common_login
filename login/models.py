from django.db import models

# Create your models here.
""" 用户表User
    用户名
    密码
    邮箱地址
    性别
    创建时间
 """


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
        ('alien', '外星人'),
    )
    # name同于用户名, 所以设为唯一
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-c_time"]
        verbose_name = '用户'
        verbose_name_plural = "用户"

    
class ConfirmString(models.Model):
    # code字段是哈希后的注册码
    code = models.CharField(max_length=256)
    # ConfirmString模型保存了用户和注册码之间的关系，一对一的形式
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":  " + self.code

    
    class Meta:
        ordering = ['-c_time']
        verbose_name = '确认码'
        verbose_name_plural = '确认码'