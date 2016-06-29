from django.contrib import admin

# Register your models here.
from models import PagUser
from models import Hotel
from models import HotelsUser
from models import Image
from models import Comment

admin.site.register(Hotel)
admin.site.register(PagUser)
admin.site.register(HotelsUser)
admin.site.register(Image)
admin.site.register(Comment)
