from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import date

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    search_query = request.GET.get("q", "")

    if search_query:
        tasks = tasks.filter(title__icontains=search_query)

    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")

        # Determine status based on due date
        due_date_obj = date.fromisoformat(due_date)
        if due_date_obj < date.today():
            status = "Overdue"
        elif due_date_obj == date.today():
            status = "Due Today"
        else:
            status = "Upcoming"

        Task.objects.create(title=title, description=description, due_date=due_date, status=status)
        return redirect("task_list")

    return render(request, "tasks/task_form.html")

def task_update(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.title = request.POST.get("title")
        task.description = request.POST.get("description")
        task.due_date = request.POST.get("due_date")

        # Recalculate status
        due_date_obj = date.fromisoformat(task.due_date)
        if due_date_obj < date.today():
            task.status = "Overdue"
        elif due_date_obj == date.today():
            task.status = "Due Today"
        else:
            task.status = "Upcoming"

        task.save()
        return redirect("task_list")

    return render(request, "tasks/task_form.html", {"task": task})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(request, "tasks/task_confirm_delete.html", {"task": task})