from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Boards Admin Panel"
admin.site.site_title = " Admin "


class InlineTopic(admin.StackedInline):
    model = Topic
    extra = 1


class TopicAdmin (admin.ModelAdmin):
    fields = ['subject', 'board', 'views',]
    list_display = ['subject', 'board',
                    'created_by',  'combine_sbuject_and_board']
    list_display_links = ['board', 'created_by',]
    list_editable = ['subject']
    list_filter = ['created_by', 'board']
    search_fields = ('board__name', 'created_by__username')

    def combine_sbuject_and_board(self, obj):
        return "{} - {}".format(obj.subject, obj.board)


class BoardAdmin(admin.ModelAdmin):
    inlines = [InlineTopic]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Board, BoardAdmin)
