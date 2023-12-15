from django.http import HttpResponse
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .models import Employee, Vacation
from .forms import EmployeeForm, VacationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def EmployeeListView(request):
    search_query = request.POST.get("search-employee")

    if search_query:
        employees = Employee.objects.filter(name__icontains=search_query)
    else:
        employees = get_list_or_404(Employee)
    return render(request, "employee_list.html", context={"employees": employees})


@login_required
def EmployeeDetailView(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, "employee_detail.html", context={"employee": employee})


@login_required
def EmployeeCreateView(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
    else:
        form = EmployeeForm()  # Move the form instantiation here

    return render(request, "employee_create.html", context={"form": form})


@login_required
def EmployeeUpdateView(request, employee_id):
    form = None
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm(instance=employee)

    return render(
        request, "employee_update.html", context={"form": form, "employee": employee}
    )


@login_required
def EmployeeDeleteView(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == "POST":
        employee.delete()
        return redirect("employee-list")
    return render(request, "employee_delete.html", context={"employee": employee})
