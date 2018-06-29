# coding=utf-8

from __future__ import unicode_literals

# from django.contrib.auth.models import User
from django.db.models import *

from blog.models import Post


class Comment(Model):
	post = ForeignKey(Post, verbose_name='文章')
	content = CharField(max_length=2000, verbose_name='内容')
	nkckname = CharField(max_length=50, verbose_name='昵称')
	website = URLField(verbose_name='网站')
	email = EmailField(verbose_name='邮箱')
	created_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')

	class Meta:
		verbose_name = verbose_name_plural = '评论'