from django.contrib import admin
from .models import modelQuestions,Claim,plan
# Register your models here.




class ClaimAdmin(admin.ModelAdmin):
    list_display = ('name', )


class modelQuestionsAdmin(admin.ModelAdmin):
    list_display = ('_id', )


class planAdmin(admin.ModelAdmin):
    list_display = ('_id', )


admin.site.register(Claim, ClaimAdmin)
admin.site.register(modelQuestions, modelQuestionsAdmin)
admin.site.register(plan, planAdmin)
