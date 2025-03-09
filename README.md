# task_manager
Django Task Manager - Setup Instructions

Project Overview
Django Task Manager is a simple CRUD (Create, Read, Update, Delete) application for managing tasks. It allows users to create, update, and delete tasks with a due date and status automatically determined based on the due date.

Installation and Setup
-Maria DB Should be 10.5 aboove

Clone the Repository
git clone <repository_url>
cd task_manager

install this using vscode terminal, 
pip install pipenv, 
pipenv install Django, 
pipenv shell, 
django-admin startproject task_manager, 
cd task_manager, 
python manage.py startapp tasks, 
pip install mysqlclient, 
pip install pymysql, 
python manage.py migrate,

Usage

Create a Task: Click on "Create New Task" and fill in the details.
Edit a Task: Click "Edit" next to a task.
Delete a Task: Click "Delete" and confirm.
Search Tasks: Use the search bar to find tasks by title.
Automatic Status:
"Due Today" if the due date is today.
"Upcoming" if the due date is in the future.
"Overdue" if the due date has passed.
