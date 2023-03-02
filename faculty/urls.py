from django.urls import path
from faculty import views

app_name = 'faculty'
urlpatterns = [

    path('',                                        views.index,                                name='index'),

    path('staff/create/',                           views.StaffCreateView.as_view(),            name='staff-create'),
    path('staff/',                                  views.StaffListView.as_view(),              name='staff-list'),
    path('staff/<int:pk>',                          views.StaffDetailView.as_view(),            name='staff-detail'),
    path('staff/edit/<int:pk>',                     views.StaffUpdateView.as_view(),            name='staff-update'),

    path('course/create/',                          views.CourseCreateView.as_view(),           name='course-create'),
    path('courses/',                                views.CourseListView.as_view(),             name='course-list'),
    path('course/<int:pk>',                         views.CourseDetailView.as_view(),           name='course-detail'),
    path('course/edit/<int:pk>',                    views.CourseUpdateView.as_view(),           name='course-update'),

    path('coursestudent/create/',                   views.CourseStudentCreateView.as_view(),    name='coursestudent-create'),
    path('coursestudent/create/course/<int:cpk>',   views.CourseStudentCreateView.as_view(),    name='coursestudent-create-cpk'),
    path('coursestudent/create/student/<int:spk>',  views.CourseStudentCreateView.as_view(),    name='coursestudent-create-spk'),
    path('coursestudent/<int:pk>',                  views.CourseStudentDetailView.as_view(),    name='coursestudent-detail'),
    path('coursestudent/delete/<int:pk>',           views.CourseStudentDeleteView.as_view(),    name='coursestudent-delete'),

    path('rooms/',                                  views.RoomsView,                            name='rooms-list'),
    path('<str:room>/schedule',                     views.RoomScheduleView,                     name='room-schedule-detail'),
    path('schedule/create/room/<str:room>',         views.ScheduleCreateView.as_view(),         name='schedule-create-rpk'),
    path('schedule/create/course/<int:course>',     views.ScheduleCreateView.as_view(),         name='schedule-create-cpk'),
    path('schedule/<int:pk>',                       views.ScheduleDetailView.as_view(),         name='schedule-detail'),
    path('schedule/edit/<int:pk>/<str:from>',       views.ScheduleUpdateView.as_view(),         name='schedule-update'),
    path('schedule/delete/<int:pk>/<str:from>',     views.ScheduleDeleteView.as_view(),         name='schedule-delete'),

]
