from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime, timedelta
import time

# Create your models here.
from django.utils.translation import gettext_lazy as _


class Nationality(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Nationality'


class State(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'State Of Origin'


class LocalGovernment(models.Model):
    name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Local Government Origin'


class Village(models.Model):
    village_Name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.village_Name

    class Meta:
        verbose_name_plural = 'Name Of Village'




class Faculty(models.Model):
    faculty = models.CharField(max_length=200, blank=False, default="1")

    def __str__(self):
        return self.faculty

    class Meta:
        verbose_name_plural = 'Name Of Faculty'

class Department(models.Model):
    name = models.CharField(max_length=200, blank=False, default="1")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Name Of Department'


class Placement(models.Model):
    admitted_class = models.CharField(max_length=200, blank=False, default="1")

    def __str__(self):
        return self.admitted_class

    class Meta:
        verbose_name_plural = 'Name Of Start Class'



class AcademicSession(models.Model):
    academic_Session  = models.CharField(max_length=200, default="2003/2024", blank=False)
   
    def __str__(self):
        return self.academic_Session

    class Meta:
        verbose_name_plural = 'Name Of Academic Session'



class Course(models.Model):
    course_Title = models.CharField(max_length=200)

    def __str__(self):
        return self.course_Title

    class Meta:
        verbose_name_plural = 'Course'


class Code(models.Model):
    course_Code = models.CharField(max_length=200)

    def __str__(self):
        return self.course_Code

    class Meta:
        verbose_name_plural = 'Course Code'



class Admission(models.Model):
        PROGRAMTYPE = [
        ('phd', 'PHD'),
        ('masters', 'Masters'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('diploma', 'Diploma'),
        ('predegree', 'Pre Degree'),
        ('default', 'Full Time'),
        
    ]

        STATUS = [
        ('accepted', 'Admitted and Accepted'),
        ('rejected', 'Admitted but Rejected'),
        ('denied', 'Not Admitted'),
        ('differed', 'Amitted But Defered'),
        ('default', 'accepted'),
        
    ]
        #program_Id = models.CharField(max_length=100, default="0001")
        #def number():
                #program_Id = Admission.objects.count()
                #if program_Id == None:
                    #return 1
                #else:
                    #return program_Id + 1
                    
        
        
        program_Id = models.CharField(max_length=200, blank=True, null=True)
        def save(self):
            if not self.program_Id and self.pk is None:
                last_program_Id = Admission.objects.count().order_by("-pk").first()
                last_pk = 0
                if last_program_Id:
                    last_pk = last_program_Id.pk
        
                self.last_program_Id = "ADMSCODE-UNICROSS_001" + str(last_pk+1).zfill(3)

            super(Admission, self).save()


        #Admissioncode = models.CharField(_('Admission_Code'), max_length=6, unique=True,\
        #default=number)
        #program_id = models.CharField(max_length=100, default="0001")
        program_type = models.CharField(choices=PROGRAMTYPE, default='Full Time', max_length=50)
        matrix_No = models.CharField(max_length=100, unique=True, default="2003/csc-0001")
        # admission_id = models.IntegerField(max_length="50", unique=True,  default="1")
        student_name = models.CharField(max_length=100)
        academic_year = models.CharField(max_length=100)
        duration = models.CharField(max_length=100, default="5")    
        admission_date = models.DateTimeField()
        admitted_class = models.ForeignKey(Placement, on_delete=models.CASCADE, default="100")
        academic_Session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, default="2003/2024")  
        status = models.CharField(choices=STATUS, default='Full Time', max_length=50)
        faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default="1")
        department = models.ForeignKey(Department, on_delete=models.CASCADE, default="1")
        
        
        def __str__(self):
                #return self.student_name + "  " + self.academic_year +"  " + self.matrix_No +" ‖ " + self.program_type +" ‖ " + self.status
                return self.matrix_No 

        class Meta:
            unique_together = ["matrix_No", "program_type"]
            verbose_name_plural = 'Admission List'

    

class Student(models.Model):
    # basif fields
        # program_Type = models.CharField(choices=PROGRAMTYPE, blank=False, max_lenght=200)
        matrix_No = models.OneToOneField(Admission, on_delete=models.CASCADE, default="2003/csc-0001")
        first_Name = models.CharField(max_length=200)
        sure_Name = models.CharField(max_length=200)
        other_Name = models.CharField(max_length=200)
        FRESHMAN = "FR"
        SOPHOMORE = "SO"
        JUNIOR = "JR"
        SENIOR = "SR"
        GRADUATE = "GR"
        YEAR_IN_SCHOOL_CHOICES = [
            (FRESHMAN, "Freshman"),
            (SOPHOMORE, "Sophomore"),
            (JUNIOR, "Junior"),
            (SENIOR, "Senior"),
            (GRADUATE, "Graduate"),
        ]
        year_in_school = models.CharField(
            max_length=2,
            choices=YEAR_IN_SCHOOL_CHOICES,
            default=FRESHMAN,
        )

        def is_upperclass(self):
            return self.year_in_school in {self.JUNIOR, self.SENIOR}

        gender_choice = (
            ("male", "Male"),
            ("Female", "Female"),
        )
        gender = models.CharField(max_length=10, choices=gender_choice, default="Male")
        date_Of_Birth = models.DateTimeField
        phone_No = models.CharField(max_length=200, unique=True, default="+234")
        email = models.CharField(max_length=200, unique=True, default="email@example.com" )
        profile_pic = models.ImageField(default = 'avatar', upload_to='profile_pic/Student/', blank=True)
        home_Address = models.CharField(max_length=40)
        nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
        state = models.ForeignKey(State, on_delete=models.CASCADE)
        local_Government = models.ForeignKey(LocalGovernment, on_delete=models.CASCADE)
        village_Name = models.ForeignKey(Village, on_delete=models.CASCADE)
        mother_Maiden_name = models.CharField(max_length=200)


        def __str__(self):
            return self.first_Name + "  " + self.sure_Name +"  " + self.other_Name +" ‖ " + self.email 

        class Meta:
            verbose_name_plural = 'Students Personal Information'
            



class CreateQuestion(models.Model):
    name_of_Department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    course_title = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    course_Code = models.ForeignKey(Code, on_delete=models.CASCADE, default=False)
    test_Question = models.CharField(max_length=200, blank=False)
    option_A = models.CharField(max_length=200, blank=False)
    option_B = models.CharField(max_length=200, blank=False)
    option_C = models.CharField(max_length=200, blank=False)
    option_D = models.CharField(max_length=200, blank=False)
    marks = models.CharField(max_length=200, blank=False)
    correct_Answer = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.test_Question

    class Meta:
        verbose_name_plural = 'Question Bank'


