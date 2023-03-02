from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [

   path('', views.index, name='index'),

   path('student/create/', views.CreateStudent, name='student-create'),
   path('student/create/<int:gpk>', views.CreateStudent, name='student-create-gpk'),
   path('students/', views.StudentListView.as_view(), name='student-list'),
   path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
   path('student/edit/<int:pk>', views.StudentUpdateView.as_view(), name='student-update'),

   path('guardian/create/', views.GuardianCreateView.as_view(), name='guardian-create'),
   path('guardian/create/<int:spk>', views.GuardianCreateView.as_view(), name='guardian-create-spk'),
   path('guardians/', views.GuardianListView.as_view(), name='guardian-list'),
   path('guardian/<int:pk>', views.GuardianDetailView.as_view(), name='guardian-detail'),
   path('guardian/edit/<int:pk>', views.GuardianUpdateView.as_view(), name='guardian-update'),

   path('registration/create/', views.RegistrationCreateView.as_view(), name='registration-create'),
   path('registration/create/<int:spk>', views.RegistrationCreateView.as_view(), name='registration-create-spk'),
   path('registrations/', views.RegistrationListView.as_view(), name='registration-list'),
   path('registration/sublist/<int:grade>', views.RegistrationSublistView.as_view(), name='registration-sublist'),
   path('registration/<int:pk>', views.RegistrationDetailView.as_view(), name='registration-detail'),
   path('registration/edit/<int:pk>', views.RegistrationUpdateView.as_view(), name='registration-update'),
   path('registration/delete/<int:pk>', views.RegistrationDeleteView.as_view(), name='registration-delete'),

   path('link_student_guardian/', views.StudentGuardianCreateView.as_view(), name='studentguardian-create'),
   path('link_student_guardian/student/<int:spk>', views.StudentGuardianCreateView.as_view(), name='studentguardian-create-spk'),
   path('link_student_guardian/guardian/<int:gpk>', views.StudentGuardianCreateView.as_view(), name='studentguardian-create-gpk'),
   path('unlink-student-guardian/<int:pk>/<str:from>', views.StudentGuardianDeleteView.as_view(), name='studentguardian-delete'),

]
