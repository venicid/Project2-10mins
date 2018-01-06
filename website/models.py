from django.db import models
from faker import Factory
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    """扩展用户资料"""
    belong_to = models.OneToOneField(to=User, related_name='profile')
    profile_image = models.FileField(upload_to='profile_image')

class Video(models.Model):
    """视频字段列表"""
    title = models.CharField(null=True, blank=True, max_length=300)   # 视频标题
    content = models.TextField(null=True)  # 视频内容
    url_image = models.URLField(null=True, blank=True)   # 视频url地址

    cover = models.FileField(upload_to='cover_image', null=True)  # 上传图片字段

    new_choice = models.BooleanField(default=False)  # 视频分类用的
    editors_choice = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# f = open('/Users/Administrator/Desktop/111.txt', 'r')
# fake = Factory.create()
#
# for url in f.readlines():
#     v = Video(
#         title=fake.text(max_nb_chars=90),
#         content=fake.text(max_nb_chars=3000),
#         url_image=url,
#         new_choice=fake.pybool(),
#         editors_choice=fake.pybool(),
#         )
#     v.save()


class Ticket(models.Model):
    """投票字段"""
    voter = models.ForeignKey(to=UserProfile, related_name="voter_tickets")
    video = models.ForeignKey(to=Video, related_name='tickets')

    VOTE_CHOICES = (
        ('like','like'),
        ('dislike', 'dislike'),
        ('normal', 'normal'),
        )

    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)

    def __str__(self):
        return str(self.id)
