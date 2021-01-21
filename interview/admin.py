from django.contrib import admin

# Register your models here.
from interview.models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator','creator_date','modified_date')
    list_display = (
        'username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
                     'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user'
    )


admin.site.register(Candidate,CandidateAdmin)