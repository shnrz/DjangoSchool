from django.shortcuts import render
from django import forms
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .forms import *

def index(request):
    return render(request, 'faculty/index.html')

class StaffCreateView(CreateView):
    model = Staff
    template_name = 'faculty/staff_create.html'
    form_class = StaffForm

class StaffListView(ListView):
    model = Staff

class StaffDetailView(DetailView):
    model = Staff
    fields = '__all__'

class StaffUpdateView(UpdateView):
    model = Staff
    form_class = StaffForm
    template_name = 'faculty/staff_update.html'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'faculty/course_create.html'

class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course
    fields = '__all__'

class CourseUpdateView(UpdateView):
    model = Course
    template_name = "faculty/course_update.html"
    form_class = CourseForm

class CourseStudentCreateView(CreateView):
    model = CourseStudent
    form_class = CourseStudentForm
    template_name = 'faculty/coursestudent_create.html'

    def get_initial(self):
        if 'spk' in self.kwargs:
            return {'student': self.kwargs['spk']}
        elif 'cpk' in self.kwargs:
            return {'course': self.kwargs['cpk']}
        else:
            return super().get_initial()

    def get_success_url(self):
        if 'spk' in self.kwargs:
            return reverse('registration:student-detail', kwargs={'pk': self.kwargs['spk']})
        elif 'cpk' in self.kwargs:
            return reverse('faculty:course-detail', kwargs={'pk': self.kwargs['cpk']})
        else:
            return reverse('faculty:index')

class CourseStudentDetailView(DetailView):
    model = CourseStudent
    fields = '__all__'

class CourseStudentDeleteView(DeleteView):
    model = CourseStudent
    template_name = "faculty/coursestudent_confirm_delete.html"

    def get_success_url(self):
        return reverse('registration:student-detail', kwargs={'pk': self.object.student.id})

def RoomsView(request):
    rooms = []
    for room in Schedule.objects.all().values('room'):
        if not room['room'] in rooms:
            rooms.append(room['room'])
    context = {}
    if len(rooms) > 0:
        rooms.sort()
        context['rooms'] = rooms
    return render(request, 'faculty/schedule_list.html', context)

def RoomScheduleView(request, *args, **kwargs):
    schedules = Schedule.objects.filter(room__exact=kwargs['room'])
    context = { 'schedules': schedules }
    return render(request, 'faculty/room_schedule.html', context)

class ScheduleCreateView(CreateView):
    model = Schedule
    template_name = "faculty/schedule_create.html"
    form_class = ScheduleForm

    def get_initial(self):
        if 'room' in self.kwargs:
            return {'room': self.kwargs['room']}
        elif 'course' in self.kwargs:
            return {'course': self.kwargs['course']}
        else:
            return super(ScheduleCreateView, self).get_initial(self)

    def get_success_url(self):
        if 'room' in self.kwargs:
            return reverse('faculty:room-schedule-detail', kwargs={'room': self.kwargs['room']})
        else:
            return reverse('faculty:course-detail', kwargs={'pk': self.kwargs['course']})

class ScheduleDetailView(DetailView):
    model = Schedule
    template_name='faculty/schedule_detail.html'

class ScheduleUpdateView(UpdateView):
    model = Schedule
    template_name = "faculty/schedule_update.html"
    form_class = ScheduleForm

    def get_success_url(self):
        if self.kwargs['from'] == 'room':
            return reverse('faculty:room-schedule-detail', kwargs={'room': self.object.room})
        else:
            return reverse('faculty:course-detail', kwargs={'pk': self.object.course.id})

class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = "faculty/schedule_delete_confirm.html"

    def get_success_url(self):
        if self.kwargs['from'] == 'course':
            return reverse('faculty:course-detail', kwargs={'pk': self.object.course.id})
        else:
            if Schedule.objects.filter(room=self.object.room).count() > 1:
                return reverse('faculty:room-schedule-detail', kwargs={'room': self.object.room})
            else:
                return reverse('faculty:rooms-list')
