from django import forms
from django.db.models import Q
from .models import *
from django_select2.forms import Select2Widget

class CourseForm(forms.ModelForm):

   def clean(self) :
      teacher = self.cleaned_data.get('teacher')
      ta1 = self.cleaned_data.get('ta_1')
      ta2 = self.cleaned_data.get('ta_2')
      if teacher == ta1 or teacher == ta2:
         self.add_error('ta_1', 'Select different staff')
      if ta1 == ta2:
         self.add_error('ta_2', 'Select different staff')

   class Meta:
      model = Course
      fields = '__all__'
      widgets = {
         'teacher':   Select2Widget(attrs={'class': 'select2-drop browser-default'}),
         'ta_1':      Select2Widget(attrs={'class': 'select2-drop browser-default'}),
         'ta_2':      Select2Widget(attrs={'class': 'select2-drop browser-default'}),
      }
      labels = {
         'ta_1':      'Teacher Assistant 1',
         'ta_2':      'Teacher Assistant 2',
      }

class CourseStudentForm(forms.ModelForm):

   class Meta:
      model = CourseStudent
      fields = '__all__'
      widgets = {
         'course': Select2Widget(attrs={'class': 'select2-drop browser-default'}),
         'student': Select2Widget(attrs={'class': 'select2-drop browser-default'})
      }

   def clean(self):
      clean_form_data = super().clean()
      course = clean_form_data['course']
      student = clean_form_data['student']
      if CourseStudent.objects.filter(course=course).filter(student=student).exists():
         raise forms.ValidationError('This student is already enrolled in this course.')

class StaffForm(forms.ModelForm):

   def clean(self):
      cleaned_data = super(CreateStaffForm, self).clean()
      if not (self.cleaned_data.get('phone_mobile_1') or self.cleaned_data.get('phone_mobile_2') or self.cleaned_data.get('phone_home')):
         self.add_error('phone_mobile_1', 'Provide at least one phone number.')
      if self.cleaned_data.get('pay_method') == 'Bank' and not self.cleaned_data.get('bank'):
         self.add_error('bank', 'Specify the payroll bank.')
      if self.cleaned_data.get('bank') and not self.cleaned_data.get('account'):
         self.add_error('account', 'Specify bank account number.')

   class Meta:
      model = Staff
      fields = [
         'first_name', 'middle_name', 'last_name_1', 'last_name_2',
         'dob', 'gender',
         'phone_mobile_1', 'phone_mobile_2', 'phone_home',
         'email',
         'address_home',
         'address_other',
         'position', 'supervisor', 'hire_date',
         'salary', 'pay_method', 'bank', 'account',
         'notes'
      ]
      widgets = {
         'supervisor': Select2Widget(attrs={'class': 'select2-drop browser-default'}),
         'address_home': forms.Textarea(attrs={'required': ''})
      }

class ScheduleForm(forms.ModelForm):

   class Meta:
      model = Schedule
      fields = '__all__'
      widgets = {
         'course': Select2Widget(attrs={'class': 'select2-drop browser-default'}),
         'start_time': forms.TextInput(attrs={'class': 'timepicker'})
      }

   def clean_end_time(self):
      start_time = self.cleaned_data.get('start_time')
      end_time = self.cleaned_data.get('end_time')
      if start_time >= end_time:
         self.add_error('end_time', 'Select a later end time.')
      return end_time

   def clean(self):
      room = self.cleaned_data.get('room')
      day = self.cleaned_data.get('weekday')
      starttime = self.cleaned_data.get('start_time')
      endtime = self.cleaned_data.get('end_time')

      has_conflict = Schedule.objects.filter(room=room, weekday=day).filter( Q(start_time__range=(starttime, endtime)) | Q(end_time__range=(starttime, endtime)) ).exists()

      if has_conflict:
         self.add_error('start_time', 'This conflicts with another schedule.')
