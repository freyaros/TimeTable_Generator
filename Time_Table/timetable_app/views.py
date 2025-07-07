from django.shortcuts import render, redirect, get_object_or_404
from .models import TimetableEntry, ClassGroup
from .forms import TimetableEntryForm, ClassGroupForm, SubjectForm, TeacherForm
from django.urls import reverse
from django.core.exceptions import ValidationError

def home(request):
    class_groups = ClassGroup.objects.all()
    return render(request, 'timetable_app/home.html', {'class_groups': class_groups})



def timetable_create(request):
    success_message = None
    if request.method == 'POST':
        form = TimetableEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            try:
                entry.full_clean()
                entry.save()
                success_message = "Timetable entry added successfully!"
                form = TimetableEntryForm()  
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = TimetableEntryForm()
    class_groups = ClassGroup.objects.all()
    return render(
        request,
        'timetable_app/timetable_create.html',
        {'form': form, 'class_groups': class_groups, 'success_message': success_message}
    )

def classgroup_timetable(request, group_id):
    class_group = get_object_or_404(ClassGroup, pk=group_id)
    entries = TimetableEntry.objects.filter(class_group=class_group).order_by('day', 'period')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    class_groups = ClassGroup.objects.all()
    return render(request, 'timetable_app/classgroup_timetable.html', {
        'class_group': class_group,
        'entries': entries,
        'days': days,
        'class_groups': class_groups,
    })

def add_class_group(request):
    if request.method == 'POST':
        form = ClassGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClassGroupForm()
    class_groups = ClassGroup.objects.all()
    return render(request, 'timetable_app/add_class_group.html', {'form': form, 'class_groups': class_groups})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubjectForm()
    class_groups = ClassGroup.objects.all()
    return render(request, 'timetable_app/add_subject.html', {'form': form, 'class_groups': class_groups})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    class_groups = ClassGroup.objects.all()
    return render(request, 'timetable_app/add_teacher.html', {'form': form, 'class_groups': class_groups})

def delete_classgroup_timetable(request, group_id):
    class_group = get_object_or_404(ClassGroup, pk=group_id)
    if request.method == 'POST':
        TimetableEntry.objects.filter(class_group=class_group).delete()
        return redirect('home')
    return render(request, 'timetable_app/delete_confirm.html', {'class_group': class_group})
