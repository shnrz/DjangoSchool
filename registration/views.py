from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse
from .models import Student, Guardian, StudentGuardian, Registration
from django import forms
from .forms import *
from datetime import date

def index(request):
   return render(request, 'registration/index.html')

def CreateStudent(request, gpk=None):

    # Submitting the filled out form.
    if request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            # Create Student object.
            student_data = {
                'first_name': form.cleaned_data['stud_fn'],
                'middle_name': form.cleaned_data['stud_mn'],
                'last_name_1': form.cleaned_data['stud_ln1'],
                'last_name_2': form.cleaned_data['stud_ln2'],
                'gender': form.cleaned_data['stud_gender'],
                'email': form.cleaned_data['stud_email'],
                'notes': form.cleaned_data['stud_notes'],
                'dob': form.cleaned_data['stud_dob'],
                'phone_mobile_1': form.cleaned_data['stud_mobile1'],
                'phone_home': form.cleaned_data['stud_phone_home']
            }
            s = Student(**student_data)
            s.save()

            # Create and associate guardians.
            if form.cleaned_data['guard1_guardian']:
                stud_guard_data = {
                    'student': s,
                    'guardian': form.cleaned_data['guard1_guardian'],
                    'relationship': form.cleaned_data['guard1_relation']
                }
                sg = StudentGuardian(**stud_guard_data)
                sg.save()
            if form.cleaned_data['guard2_guardian']:
                stud_guard_data = {
                    'student': s,
                    'guardian': form.cleaned_data['guard2_guardian'],
                    'relationship': form.cleaned_data['guard2_relation']
                }
                sg = StudentGuardian(**stud_guard_data)
                sg.save()
            if form.cleaned_data['guard3_fn']:
                guardian_data = {
                    'first_name': form.cleaned_data['guard3_fn'],
                    'middle_name': form.cleaned_data['guard3_mn'],
                    'last_name_1': form.cleaned_data['guard3_ln1'],
                    'last_name_2': form.cleaned_data['guard3_ln2'],
                    'gender': form.cleaned_data['guard3_gender'],
                    'email': form.cleaned_data['guard3_email'],
                    'notes': form.cleaned_data['guard3_notes'],
                    'phone_mobile_1': form.cleaned_data['guard3_phone_mobile1'],
                    'phone_mobile_2': form.cleaned_data['guard3_phone_mobile2'],
                    'phone_home': form.cleaned_data['guard3_phone_home'],
                    'phone_work': form.cleaned_data['guard3_phone_work'],
                    'address_home': form.cleaned_data['guard3_address_home'],
                    'address_work': form.cleaned_data['guard3_address_work'],
                    'address_other': form.cleaned_data['guard3_address_other']
                }
                guard3 = Guardian(**guardian_data)
                guard3.save()
                stud_guard_data = {
                    'student': s,
                    'guardian': guard3,
                    'relationship': form.cleaned_data['guard3_relation']
                }
                sg = StudentGuardian(**stud_guard_data)
                sg.save()
            if form.cleaned_data['guard4_fn']:
                guardian_data = {
                    'first_name': form.cleaned_data['guard4_fn'],
                    'middle_name': form.cleaned_data['guard4_mn'],
                    'last_name_1': form.cleaned_data['guard4_ln1'],
                    'last_name_2': form.cleaned_data['guard4_ln2'],
                    'gender': form.cleaned_data['guard4_gender'],
                    'email': form.cleaned_data['guard4_email'],
                    'notes': form.cleaned_data['guard4_notes'],
                    'phone_mobile_1': form.cleaned_data['guard4_phone_mobile1'],
                    'phone_mobile_2': form.cleaned_data['guard4_phone_mobile2'],
                    'phone_home': form.cleaned_data['guard4_phone_home'],
                    'phone_work': form.cleaned_data['guard4_phone_work'],
                    'address_home': form.cleaned_data['guard4_address_home'],
                    'address_work': form.cleaned_data['guard4_address_work'],
                    'address_other': form.cleaned_data['guard4_address_other']
                }
                guard4 = Guardian(**guardian_data)
                guard4.save()
                stud_guard_data = {
                    'student': s,
                    'guardian': guard4,
                    'relationship': form.cleaned_data['guard4_relation']
                }
                sg = StudentGuardian(**stud_guard_data)
                sg.save()
            return HttpResponseRedirect(reverse('registration:student-detail', kwargs={ 'pk': s.id }))

    # Getting a fresh form for filling out.
    else:
        if gpk:
            form = CreateStudentForm(initial={'guard1_guardian': Guardian.objects.get(id=gpk)})
        else:
            form = CreateStudentForm()

    return render(request, 'registration/student_create.html', {'form': form})

class StudentDetailView(generic.DetailView):
    model = Student

class StudentListView(generic.ListView):
    model = Student

class StudentUpdateView(generic.UpdateView):
    model = Student
    template_name = "registration/student_update.html"
    form_class = UpdateStudentForm

class GuardianCreateView(generic.CreateView):
    model = Guardian
    form_class = CreateGuardianForm
    template_name = "registration/guardian_create.html"

    def get_initial(self):
        if 'spk' in self.kwargs:
            return {'student_1': Student.objects.get(id=self.kwargs['spk'])}
        else:
            return super().get_initial()

    def form_valid(self, form):
        self.object = form.save()
        if form.cleaned_data['student_1']:
            stud_guard_data = {
                'student': form.cleaned_data['student_1'],
                'guardian': self.object,
                'relationship': form.cleaned_data['stud1_relation']
            }
            sg = StudentGuardian(**stud_guard_data)
            sg.save()
        if form.cleaned_data['student_2']:
            stud_guard_data = {
                'student': form.cleaned_data['student_2'],
                'guardian': self.object,
                'relationship': form.cleaned_data['stud2_relation']
            }
            sg = StudentGuardian(**stud_guard_data)
            sg.save()
        if form.cleaned_data['new_student_after']:
            form = CreateStudentForm(initial={'guard1_guardian': self.object})
            ctx = {
                'form': form
            }
            return render(self.request, 'registration/student_create.html', ctx)
        return HttpResponseRedirect(self.get_success_url())

class GuardianListView(generic.ListView):
    model = Guardian

class GuardianDetailView(generic.DetailView):
    model = Guardian

class GuardianUpdateView(generic.UpdateView):
    model = Guardian
    template_name = "registration/guardian_update.html"
    fields = '__all__'

class RegistrationCreateView(generic.CreateView):
    model = Registration
    template_name = "registration/registration_create.html"
    form_class = CreateRegistrationForm

    def get_initial(self):
        if 'spk' in self.kwargs:
            return {'student': Student.objects.get(id=self.kwargs['spk'])}
        else:
            return super().get_initial()

    # def form_valid(self, form):
    #     if form.cleaned_data['is_active']:
    #         stud_registrations = Registration.objects.filter(student_id=form.cleaned_data['student'].id).filter(is_active=True)
    #         for reg in stud_registrations:
    #             reg.is_active = False
    #             reg.save()
    #     return super().form_valid(form)

class RegistrationListView(generic.ListView):
    model = Registration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["registration_counts"] = {
            'Prekinder': 0,
            'Kinder': 0,
            '1': 0,
            '2': 0,
            '3': 0,
            '4': 0,
            '5': 0,
            '6': 0,
            '7': 0,
            '8': 0,
            '9': 0,
            '10': 0,
            '11': 0
        }
        for registration in Registration.objects.all():
            context['registration_counts'][str(registration.grade)] += 1
        return context

class RegistrationSublistView(generic.ListView):
    model = Registration
    template_name = "registration/registration_sublist.html"

    def get_queryset(self):
        reg_list = Registration.objects.filter(grade=self.kwargs['grade'])
        return reg_list

class RegistrationDetailView(generic.DetailView):
    model = Registration

class RegistrationUpdateView(generic.UpdateView):
    model = Registration
    template_name = "registration/registration_update.html"
    form_class = UpdateRegistrationForm

    def form_valid(self, form):
        if form.cleaned_data['is_active']:
            stud_registrations = Registration.objects.filter(student_id=form.cleaned_data['student'].id).filter(is_active=True)
            for reg in stud_registrations:
                reg.is_active = False
                reg.save()
        return super().form_valid(form)

class RegistrationDeleteView(generic.DeleteView):
    model = Registration

    def get_success_url(self):
        return reverse_lazy('registration:student-detail', kwargs={'pk': self.object.student_id})

class StudentGuardianCreateView(generic.CreateView):
    model = StudentGuardian
    form_class = CreateStudentGuardianForm
    template_name = "registration/studentguardian_create.html"
    success_url = '/'

    def get_initial(self):
        prefill_data = {}
        if 'spk' in self.kwargs:
            prefill_data['student'] = Student.objects.get(id=self.kwargs['spk'])
        if 'gpk' in self.kwargs:
            prefill_data['guardian'] = Guardian.objects.get(id=self.kwargs['gpk'])
        if ('spk' in self.kwargs or 'gpk' in self.kwargs):
            return prefill_data
        else:
            return super().get_initial()

    def get_success_url(self):
        if 'gpk' in self.kwargs:
            return reverse('registration:guardian-detail', kwargs={'pk': self.object.guardian_id})
        else:
            return reverse('registration:student-detail', kwargs={'pk': self.object.student_id})

class StudentGuardianDeleteView(generic.DeleteView):
    model = StudentGuardian
    success_url = '/'

    def get_success_url(self):
        if (self.kwargs['from'] == 'student'):
            return reverse_lazy('registration:student-detail', kwargs={'pk': self.object.student_id})
        else:
            return reverse_lazy('registration:guardian-detail', kwargs={'pk': self.object.guardian_id})
