from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Collaborator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CollaboratorForm, DepartmentForm

def home(request):
    return render(request, 'base.html')

def collaborator_list(request):
    collaborators = Collaborator.objects.all()
    return render(request, 'collaborator_list.html', {'collaborators': collaborators})

@csrf_exempt
def collaborator_add(request):
    if request.method == 'POST':
        form = CollaboratorForm(request.POST)
        if form.is_valid():
            collaborator = form.save()
            return redirect('collaborator_list')
    else:
        form = CollaboratorForm()
    return render(request, 'collaborator_form.html', {'form': form})

@csrf_exempt
def collaborator_remove(request, pk):
    collaborator = get_object_or_404(Collaborator, pk=pk)
    collaborator.delete()
    return redirect('collaborator_list')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

@csrf_exempt
def department_add(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

@csrf_exempt
def department_remove(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect('department_list')