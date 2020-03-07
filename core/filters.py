from rest_framework import filters

class CourseFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        """
        Get a list of all courses, telling which ones the student can access
        required id student in the request
        """
        return queryset

class LessonFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        """
        Get lessons for a course, telling which ones the student can access
        required id student in the request
        """
        return queryset