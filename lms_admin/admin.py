from django.contrib import admin

from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple

from profiles.models import UserDegree

#admin.site.register(User)


class DegreeInLine(admin.StackedInline):
	model = UserDegree
	extra = 1


class AdUserAdmin(UserAdmin):
	inlines = [
		DegreeInLine,
	]
	def get_form(self, request, obj=None, **kwargs):
		form = super(AdUserAdmin,self).get_form(request, obj, **kwargs)
		try:
			groups: form.base_field['groups']
			groups.widget = FilteredSelectMultiple("Groups", False)

		except KeyError:
			pass
		return form
		

