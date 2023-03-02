from datetime import date, datetime
from django.db import models
from registration.models import Person, Student
from django.urls import reverse

class Staff(Person):

    dob =               models.DateField(verbose_name='Date of birth')
    phone_mobile_1 =    models.CharField(max_length=15, blank=True)
    phone_mobile_2 =    models.CharField(max_length=15, blank=True)
    phone_home =        models.CharField(max_length=15, blank=True)
    address_home =      models.TextField(max_length=500)
    address_other =     models.TextField(max_length=500, blank=True)
    position =          models.CharField(max_length=100)
    supervisor =        models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    hire_date =         models.DateField(blank=True, default=datetime.now)
    salary =            models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=8)
    pay_method =        models.CharField(max_length=50, choices=[('Bank', 'Bank'), ('Check', 'Check'), ('Cash', 'Cash')], default='Bank')
    bank =              models.CharField(max_length=20, choices=[('BAC', 'BAC'), ('BDF', 'BDF'), ('BANPRO', 'BANPRO'), ('LAFISE', 'LAFISE'), ('FICOHSA', 'FICOHSA'), ('BANCORP', 'BANCORP')], blank=True)
    account =           models.CharField(max_length=50, blank=True)

    def __str__(self):
        str = self.last_name_1
        if self.last_name_2:
            str += ' ' + self.last_name_2 + ', '
        else:
            str += ', '
        str += self.first_name
        if self.middle_name:
            str += ' ' + self.middle_name
        return str

    def get_absolute_url(self):
        return reverse("faculty:staff-detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = 'Staff'

class Semester(models.Model):

    year = models.IntegerField(default=int(datetime.now().strftime('%Y')))
    number = models.IntegerField(choices=[(1,'First'), (2,'Second')])
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(verbose_name='Is active', default=True)

    class Meta:
        verbose_name = ("Semester")
        verbose_name_plural = ("Semesters")

    def __str__(self):
        s = str(self.year)
        if self.number == 1:
            s = 'First ' + s
        else:
            s = 'Second ' + s
        return s

    def get_absolute_url(self):
        return reverse("faculty:semester-detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
       if self.is_active:
           for semester in Semester.objects.all():
               semester.is_active = False
       super(Semester, self).save(*args, **kwargs)

class Course(models.Model):

    name =      models.CharField(max_length=100)
    grade =     models.IntegerField()
    teacher =   models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='teacher_course')
    ta_1 =      models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True, related_name='ta1_course')
    ta_2 =      models.ForeignKey(Staff, on_delete=models.SET_NULL, blank=True, null=True, related_name='ta2_course')
    semester =  models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=True, null=True)
    syllabus =  models.FileField(upload_to='syllabi', blank=True, null=True)

    class Meta:
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("faculty:course-detail", kwargs={"pk": self.pk})

class CourseStudent(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Enrollment")
        verbose_name_plural = ("Enrollments")

    def __str__(self):
        return str(self.course) +  ' - ' + str(self.student)

    def get_absolute_url(self):
        return reverse("faculty:coursestudent-detail", kwargs={"pk": self.pk})

class Schedule(models.Model):

    def get_weekday(self):
        if self.weekday == 1:
            return 'Monday'
        elif self.weekday == 2:
            return 'Tuesday'
        elif self.weekday == 3:
            return 'Wednesday'
        elif self.weekday == 4:
            return 'Thursday'
        elif self.weekday == 5:
            return 'Friday'
        elif self.weekday == 6:
            return 'Saturday'
        elif self.weekday == 7:
            return 'Sunday'
        else:
            return 'Error'

    weekday = models.IntegerField(choices=[(1,'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, choices=[('Auditory', 'Auditory'), ('Room A', 'Room A'), ('Room B', 'Room B'), ('Room C', 'Room C'), ('Gym', 'Gym')])
    course = models.ForeignKey('Course', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        day = {
            1: 'MON',
            2: 'TUE',
            3: 'WED',
            4: 'THU',
            5: 'FRI',
            6: 'SAT',
            7: 'SUN'
        }
        time = self.start_time.strftime("%I%p")
        return day[self.weekday] + ' ' + time + ' ' + self.room

    def get_absolute_url(self):
        return reverse("faculty:schedule-detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ['weekday', 'start_time']
