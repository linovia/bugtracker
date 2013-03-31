from django.contrib import admin

from bugtracker.core.models import Project, Bug, Comment


class ProjectAdmin(admin.ModelAdmin):
    pass


class BugAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Bug, BugAdmin)
admin.site.register(Comment, CommentAdmin)
