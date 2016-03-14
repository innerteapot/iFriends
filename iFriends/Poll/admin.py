from django.contrib import admin
from iFriends.Poll.models import Opinion, UserPoll

# Register your models here.

#  edit_inline=models.TABULAR, num_in_admin=4
class OpinionInline(admin.TabularInline):
    model = Opinion

@admin.register(UserPoll)
class UserPollAdmin(admin.ModelAdmin):
    inlines = [
        OpinionInline,
    ]
    min_num = 4
