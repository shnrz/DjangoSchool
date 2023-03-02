from django.contrib import admin
from .models import Person, Student, Guardian, Registration, StudentGuardian

# Register your models here.
admin.site.register(Student)
admin.site.register(Guardian)
admin.site.register(Registration)
admin.site.register(StudentGuardian)
