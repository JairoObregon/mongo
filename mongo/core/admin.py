from django.contrib import admin
from .models import Answer,Question,Claim
# Register your models here.

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', )


class ClaimAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Answer, AnswerAdmin)

admin.site.register(Claim, ClaimAdmin)
