from django.urls import path

from testing_manage.views import Index, CustomLoginView, FilesListView, DownFile, FilesAddView, \
    MonkeyReportView

urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('login/', CustomLoginView.as_view(), name='login'),
    # Files
    path('files/', FilesListView.as_view(), name='files-list'),
    path('files_add/', FilesAddView.as_view(), name='files-add'),
    path('download_file/<int:id>/', DownFile.as_view(), name='download-file'),
    # report
    path('monkey_report/<str:car_name>/', MonkeyReportView.as_view(), name='monkey-report'),
]
