""" Django的表单给我们提供了下面三个主要功能：
准备和重构数据用于页面渲染；
为数据创建HTML表单元素；
接收和处理用户从表单发送过来的数据。
编写Django的form表单，非常类似我们在模型系统里编写一个模型。
在模型中，一个字段代表数据表的一列，而form表单中的一个字段代表<form>中的一个<input>元素。 """
""" 顶部要先导入forms模块
    所有的表单类都要继承forms.Form类
    每个表单字段都有自己的字段类型比如CharField，它们分别对应一种HTML语言中<form>内的一个input元素。这一点和Django模型系统的设计非常相似。
    label参数用于设置<label>标签
    max_length限制字段输入的最大长度。它同时起到两个作用，一是在浏览器页面限制用户输入不可超过字符数，二是在后端服务器验证用户输入的长度也不可超过。
widget=forms.PasswordInput用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。 """




from django import forms
class UserForm(forms.Form):

    username = forms.CharField(
        label='用户名', max_length='128', widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Username', 'autofocus': ''}))
    password = forms.CharField(
        label='密码', max_length='256', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))