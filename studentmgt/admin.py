from django.contrib import admin
from .models import Nationality
from .models import State
from .models import LocalGovernment
from .models import Village
from .models import Faculty
from .models import Department
from .models import Admission
from .models import Student
from .models import Course
from .models import Code
from .models import CreateQuestion
from .models import Placement
from .models import AcademicSession


# Register your models here.

admin.site.register(Nationality)
admin.site.register(State)
admin.site.register(LocalGovernment)
admin.site.register(Village)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Admission)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Code)
admin.site.register(CreateQuestion)
admin.site.register(Placement)
admin.site.register(AcademicSession)
