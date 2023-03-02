from django.db import models
from django.urls import reverse
from datetime import date

class Person(models.Model):

   first_name = models.CharField(max_length=50)
   middle_name = models.CharField(max_length=50, blank=True)
   last_name_1 = models.CharField(max_length=50)
   last_name_2 = models.CharField(max_length=50, blank=True)

   MALE = 'M'
   FEMALE = 'F'
   GENDER_CHOICES = [
      (MALE, 'Male'),
      (FEMALE, 'Female')
   ]
   gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

   email = models.EmailField(max_length=100, blank=True)
   notes = models.TextField(max_length=1000, blank=True)

   def __str__(self):
      return self.last_name_1 + ' ' + self.last_name_2 + ', ' + self.first_name + ' ' + self.middle_name

   class Meta:
      abstract = True
      ordering = ['last_name_1', 'last_name_2', 'first_name', 'middle_name']

class Guardian(Person):

   phone_mobile_1 = models.CharField(max_length=15, blank=True)
   phone_mobile_2 = models.CharField(max_length=15, blank=True)
   phone_home = models.CharField(max_length=15, blank=True)
   phone_work = models.CharField(max_length=15, blank=True)
   address_home = models.TextField(max_length=500, blank=True)
   address_work = models.TextField(max_length=500, blank=True)
   address_other = models.TextField(max_length=500, blank=True)

   def get_absolute_url(self):
       return reverse("registration:guardian-detail", args=[str(self.id)])

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

class Student(Person):

   dob = models.DateField(verbose_name='Date of birth')
   phone_mobile_1 = models.CharField(max_length=15, blank=True)
   phone_home = models.CharField(max_length=15, blank=True)
   guardians = models.ManyToManyField(Guardian, through='StudentGuardian', related_name='students')

   def get_absolute_url(self):
       return reverse("registration:student-detail", kwargs={'pk': self.pk})

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

class Registration(models.Model):

   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   registration_date = models.DateField(default=date.today)
   grade = models.IntegerField()
   notes = models.TextField(max_length=1000, blank=True, default='')
   is_active = models.BooleanField(verbose_name=('Is active'), default=True)

   def __str__(self):
      s = 'Grade ' + str(self.grade) + ' (' + self.registration_date.strftime('%Y') + ')'
      if self.is_active:
         s = s + ' - active'
      return s

   def get_absolute_url(self):
       return reverse("registration:registration-detail", kwargs={"pk": self.pk})

   def save(self, *args, **kwargs):
      if self.is_active:
         for registration in self.student.registration_set.all():
            registration.is_active = False
      super(Registration, self).save(*args, **kwargs)

class StudentGuardian(models.Model):
   student = models.ForeignKey(Student, related_name='student_guardian', on_delete=models.CASCADE)
   guardian = models.ForeignKey(Guardian, related_name='student_guardian', on_delete=models.CASCADE)
   relationship = models.CharField(max_length=50, default='Parent')

   def __str__(self):
      return str(self.relationship)
