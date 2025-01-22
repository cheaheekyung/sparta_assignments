from django.contrib import admin
from .models import Articles, Comment

# 모델 등록
admin.site.register(Articles)
admin.site.register(Comment)
