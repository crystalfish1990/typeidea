# coding=utf-8
from __future__ import unicode_literals

from django.db.models import *
from django.contrib.auth.models import User


class Links(Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除'),
    )

    title = CharField(max_length=50, verbose_name='标题')
    href = URLField(verbose_name='连接')  # 默认长度200
    status = PositiveIntegerField(
        default=1,
        choices=STATUS_ITEMS,
        verbose_name='状态')
    weight = PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
								  verbose_name='权重',
								  help_text='权重越高展示顺序越靠前')

    owner = ForeignKey(User, verbose_name='作者')
    created_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '友链'


class SideBar(Model):
    STATUS_ITEMS = (
        (1, '展示'),
        (2, '下线'),
    )

    SIDE_TYPE = (
                (1, 'HTML'),
                (2, '最新文章'),
                (3, '最热文章'),
                (4, '最近评论'),
    )

    title = CharField(max_length=50, verbose_name='标题')
    display_type = PositiveIntegerField(
        default=1, choices=SIDE_TYPE, verbose_name='展示类型')
    content = CharField(
        max_length=500,
        blank=True,
        verbose_name='内容',
        help_text='如果设置的不是HTML类型, 可以为空')
    owner = ForeignKey(User, verbose_name='作者')
    created_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'
