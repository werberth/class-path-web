from django.views import generic
from django.shortcuts import get_object_or_404

from . import models


class BaseInstitutionQuerysetView:
    def get_queryset(self):
        institution = self.request.user.admin.institution
        queryset = self.model.objects.filter(institution=institution)
        return queryset


class ListCourseBase(generic.ListView):
    model = models.Course
    context_object_name = 'courses'
    template_name = 'accounts/course/course_list.html'


class ListStudentBase:
    context_object_name = 'students'
    template_name = 'accounts/student/student_list.html'

    def get_context_data(self,**kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['class'] = self.get_object()
        return kwargs

    def get_queryset(self):
        _class = self.get_object()
        return _class.students.filter(is_active=True)
