from django.urls import path
from . import views

urlpatterns = [
    path("", views.EmployeeListView, name="employee-list"),
    path("<int:employee_id>", views.EmployeeDetailView, name="employee-detail"),
    path("create", views.EmployeeCreateView, name="employee-create"),
    path(
        "update/<int:employee_id>",
        views.EmployeeUpdateView,
        name="employee-update",
    ),
    path(
        "delete/<int:employee_id>",
        views.EmployeeDeleteView,
        name="employee-delete",
    ),
    path(
        "vacation/<int:employee_id>/", views.VacationCreateView, name="vacation-create"
    ),
]
