from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
	model = Member

    
admin.site.register(Member, MemberAdmin)
