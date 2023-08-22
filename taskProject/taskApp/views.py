from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from taskApp.models import Objective


def show_start_page(request, ):
    objective = Objective.objects.order_by('date', '-level')
    objective_done = Objective.objects.order_by('-level')
    context = {'objective': objective,
               'objective_done': objective_done}
    return render(request, 'main.html', context=context)


def show_create_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        level = request.POST.get('level')
        status = request.POST.get('status')

        status = True if status == 'on' else False

        Objective.objects.create(name=name,
                                 description=description,
                                 date=date,
                                 level=level,
                                 status=status)

    return render(request, 'createTask.html')


def edit_task_show_page(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date = request.POST.get('date')
        level = request.POST.get('level')
        status = request.POST.get('status')

        status = True if status == 'on' else False

        Objective.objects.filter(pk=pk).update(
            name=name,
            description=description,
            date=date,
            level=level,
            status=status
        )

    tasks = Objective.objects.get(pk=pk)
    context = {'tasks': tasks}

    return render(request, 'editTask.html', context=context)


def delete_task(request, pk):
    Objective.objects.get(pk=pk).delete()
    return redirect('http://127.0.0.1:8000')


def is_done(request, pk):
    done = Objective.objects.get(pk=pk)
    done.status = True
    done.save()
    return redirect('http://127.0.0.1:8000' )
