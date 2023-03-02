import datetime
from django import forms
from django.core.validators import MaxValueValidator
from registration.models import Person, Student, Guardian, StudentGuardian, Registration
from faculty.models import CourseStudent, Course
from django_select2.forms import Select2Widget

class CreateStudentForm(forms.Form):

   stud_fn = forms.CharField(label='First name', max_length=50, required=True)
   stud_mn = forms.CharField(label='Middle name', max_length=50, required=False)
   stud_ln1 = forms.CharField(label='Last name 1', max_length=50, required=True)
   stud_ln2 = forms.CharField(label='Last name 2', max_length=50, required=False)
   stud_gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), required=True, label='Gender')
   stud_dob = forms.DateField(required=True, label='Date of Birth', validators=[MaxValueValidator(datetime.date.today() - datetime.timedelta(days=730), 'Student is too young.')])
   stud_mobile1 = forms.CharField(label='Phone Mobile', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   stud_phone_home = forms.CharField(label='Phone Home', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   stud_email = forms.EmailField(label='Email', required=False)
   stud_notes = forms.CharField(label='Notes', max_length=1000, widget=forms.Textarea(), required=False)

   guard1_guardian = forms.ModelChoiceField(queryset=Guardian.objects.all(), widget=Select2Widget(attrs={'class': 'select2-drop browser-default'}), label='Guardian 1', required=False)
   guard1_relation = forms.CharField(max_length=100, required=False)

   guard2_guardian = forms.ModelChoiceField(queryset=Guardian.objects.all(), widget=forms.Select(attrs={'class': 'select2-drop browser-default'}), label='Guardian 2', required=False)
   guard2_relation = forms.CharField(max_length=100, required=False)

   guard3_fn = forms.CharField(label='First name', max_length=50, required=False)
   guard3_mn = forms.CharField(label='Middle name', max_length=50, required=False)
   guard3_ln1 = forms.CharField(label='Last name 1', max_length=50, required=False)
   guard3_ln2 = forms.CharField(label='Last name 2', max_length=50, required=False)
   guard3_gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), required=False, label='Gender')
   guard3_relation = forms.CharField(max_length=50, required=False, label='Relation to student')
   guard3_phone_mobile1 = forms.CharField(label='Phone Mobile 1', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard3_phone_mobile2 = forms.CharField(label='Phone Mobile 2', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard3_phone_home = forms.CharField(label='Phone Home', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard3_phone_work = forms.CharField(label='Phone Work', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard3_email = forms.EmailField(label='Email', required=False)
   guard3_address_home = forms.CharField(label='Address Home', max_length=500, required=False)
   guard3_address_work = forms.CharField(label='Address Work', max_length=500, required=False)
   guard3_address_other = forms.CharField(label='Address Other', max_length=500, required=False)
   guard3_notes = forms.CharField(label='Notes', max_length=1000, widget=forms.Textarea(), required=False)

   guard4_fn = forms.CharField(label='First name', max_length=50, required=False)
   guard4_mn = forms.CharField(label='Middle name', max_length=50, required=False)
   guard4_ln1 = forms.CharField(label='Last name 1', max_length=50, required=False)
   guard4_ln2 = forms.CharField(label='Last name 2', max_length=50, required=False)
   guard4_gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')), required=False, label='Gender')
   guard4_relation = forms.CharField(max_length=50, required=False, label='Relation to student')
   guard4_phone_mobile1 = forms.CharField(label='Phone Mobile 1', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard4_phone_mobile2 = forms.CharField(label='Phone Mobile 2', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard4_phone_home = forms.CharField(label='Phone Home', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard4_phone_work = forms.CharField(label='Phone Work', max_length=15, required=False, widget=forms.NumberInput(attrs={'min': 10000000}))
   guard4_email = forms.EmailField(label='Email', required=False)
   guard4_address_home = forms.CharField(label='Address Home', max_length=500, required=False)
   guard4_address_work = forms.CharField(label='Address Work', max_length=500, required=False)
   guard4_address_other = forms.CharField(label='Address Other', max_length=500, required=False)
   guard4_notes = forms.CharField(label='Notes', max_length=1000, widget=forms.Textarea(), required=False)

   def clean_stud_dob(self):
      dob_data = self.cleaned_data['stud_dob']
      if (dob_data > (datetime.date.today() - datetime.timedelta(days=730))):
         raise self.add_error('stud_dob', 'Student is too young.')
      return dob_data

   def clean(self):

      cleaned_data = super().clean()

      # Linked guardian 1 required fields.
      if cleaned_data.get("guard1_guardian") and not cleaned_data.get("guard1_relation"):
         self.add_error('guard1_relation', 'Relation must be specified')
      if not cleaned_data.get("guard1_guardian") and cleaned_data.get("guard1_relation"):
         self.add_error('guard1_guardian', 'A guardian must be selected')

      # Linked guardian 2 required fields.
      if cleaned_data.get("guard2_guardian") and not cleaned_data.get("guard2_relation"):
         self.add_error('guard2_relation', 'Relation must be specified')
      if not cleaned_data.get("guard2_guardian") and cleaned_data.get("guard2_relation"):
         self.add_error('guard2_guardian', 'A guardian must be selected')

      # New guardian 3 required fields.
      if cleaned_data.get("guard3_fn"):
         if not cleaned_data.get("guard3_ln1"):
            self.add_error('guard3_ln1', 'Please enter last name.')
         if not cleaned_data.get("guard3_relation"):
            self.add_error('guard3_relation', 'Please specify relation to student.')
         if not (cleaned_data.get("guard3_phone_mobile1") or cleaned_data.get("guard3_phone_mobile2") or cleaned_data.get("guard3_phone_home") or cleaned_data.get("guard3_phone_work")):
            self.add_error("guard3_phone_mobile1", 'Please enter at least 1 phone number.')

      # New guardian 4 required fields.
      if cleaned_data.get("guard4_fn"):
         if not cleaned_data.get("guard4_ln1"):
            self.add_error('guard4_ln1', 'Please enter last name.')
         if not cleaned_data.get("guard4_relation"):
            self.add_error('guard4_relation', 'Please specify relation to student.')
         if not (cleaned_data.get("guard4_phone_mobile1") or cleaned_data.get("guard4_phone_mobile2") or cleaned_data.get("guard4_phone_home") or cleaned_data.get("guard4_phone_work")):
            self.add_error("guard4_phone_mobile1", 'Please enter at least 1 phone number.')

      # At least 1 guardian provided.
      guard1_exists = False
      if cleaned_data.get("guard1_guardian") and cleaned_data.get("guard1_relation"):
         guard1_exists = True
      guard2_exists = False
      if cleaned_data.get("guard2_guardian") and cleaned_data.get("guard1_relation"):
         guard2_exists = True
      guard3_exists = False
      if cleaned_data.get("guard3_fn") and cleaned_data.get("guard3_ln1") and cleaned_data.get("guard3_relation") and (cleaned_data.get("guard3_mobile1") or cleaned_data.get("guard3_mobile2") or cleaned_data.get("guard3_phone_home") or cleaned_data.get("guard3_phone_work")):
         guard3_exists = True
      guard4_exists = False
      if cleaned_data.get("guard4_fn") and cleaned_data.get("guard4_ln1") and cleaned_data.get("guard4_relation") and (cleaned_data.get("guard4_mobile1") or cleaned_data.get("guard4_mobile2") or cleaned_data.get("guard4_phone_home") or cleaned_data.get("guard4_phone_work")):
         guard4_exists = True
      if not (guard1_exists or guard2_exists or guard3_exists or guard4_exists):
         raise forms.ValidationError("You need to create or associate at least 1 guardian for this student.")

class UpdateStudentForm(forms.ModelForm):

   class Meta:
      model = Student
      fields = [
         'first_name', 'middle_name', 'last_name_1', 'last_name_2',
         'dob', 'gender', 'phone_mobile_1', 'phone_home',
         'email',
         'guardians',
         'notes'
      ]

class CreateGuardianForm(forms.ModelForm):

   student_1 = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'select2-drop browser-default'}), label='Student 1', required=False)
   stud1_relation = forms.CharField(max_length=100, required=False, label='Relation to student')
   student_2 = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'select2-drop browser-default'}), label='Student 2', required=False)
   stud2_relation = forms.CharField(max_length=100, required=False, label='Relation to student')
   new_student_after = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'filled-in'}), label='Create a new student that is linked to this guardian')

   field_order = [
      'first_name', 'middle_name', 'last_name_1', 'last_name_2',
      'phone_mobile_1', 'phone_mobile_2', 'phone_home', 'phone_work',
      'gender', 'email',
      'address_home',
      'address_work',
      'address_other',
      'notes',
      'student_1', 'stud1_relation',
      'student_2', 'stud2_relation',
      'new_student_after'
      ]

   class Meta:
      model = Guardian
      fields = '__all__'

   def clean(self):
      cleaned_data = super().clean()
      if not (cleaned_data.get("phone_mobile_1") or cleaned_data.get("phone_mobile_2") or cleaned_data.get("phone_home") or cleaned_data.get("phone_work")):
         self.add_error('phone_mobile_1', 'Provide at least one phone number.')
      if not (cleaned_data.get("address_home") or cleaned_data.get("address_work") or cleaned_data.get("address_other")):
         self.add_error('address_home', 'Provide at least one address.')
      if (cleaned_data.get('student_1') and not cleaned_data.get('stud1_relation')):
         self.add_error('stud1_relation', 'Specify the relation of the guardian to the student.')
      if (cleaned_data.get('stud1_relation') and not cleaned_data.get('student_1')):
         self.add_error('student_1', 'Select a student.')
      if (cleaned_data.get('student_2') and not cleaned_data.get('stud2_relation')):
         self.add_error('stud2_relation', 'Specify the relation of the guardian to the student.')
      if (cleaned_data.get('stud2_relation') and not cleaned_data.get('student_2')):
         self.add_error('student_2', 'Select a student.')

class CreateRegistrationForm(forms.ModelForm):

   class Meta:
      model = Registration
      fields = '__all__'
      widgets = {
         'student': forms.Select(attrs={'class': 'select2-drop browser-default'}),
         'grade': forms.Select(attrs={'class': 'select2-drop browser-default'}, choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'))),
         'is_active': forms.CheckboxInput(attrs={'class': 'filled-in'})
      }
      labels = {
         'is_active': "Make this the student's active registration"
      }

class UpdateRegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
           'student': forms.Select(attrs={'class': 'select2-drop browser-default'}),
           'is_active': forms.CheckboxInput(attrs={'class': 'filled-in'})
        }

class CreateStudentGuardianForm(forms.ModelForm):

    class Meta:
        model = StudentGuardian
        fields = '__all__'
        widgets = {
           'student': forms.Select(attrs={'class': 'select2-drop browser-default'}),
           'guardian': forms.Select(attrs={'class': 'select2-drop browser-default'})
        }
