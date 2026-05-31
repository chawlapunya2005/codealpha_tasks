# TaskFlow — Project Management Tool
### CodeAlpha Internship — Task 3

A full-stack project management app (like Trello/Asana) built with Django.

## Features
- Create & manage projects with color labels
- Kanban board (To Do / In Progress / Done)
- Add tasks with priority, due date, and assignment
- Move tasks between columns
- Comment on tasks
- Add team members to projects
- User registration & login
- Admin panel

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

---

## Setup & Run (Windows)

### Step 1 — Install Django
```
pip install django
```

### Step 2 — Navigate to project folder
```
cd path\to\project_management
```

### Step 3 — Run migrations
```
python manage.py migrate
```

### Step 4 — Start server
```
python manage.py runserver
```

### Step 5 — Open browser
- **App:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/

---

## Demo Accounts
| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Superuser |
| alice | demo123 | Member |
| bob | demo123 | Member |

## GitHub Repo Name
`CodeAlpha_ProjectManagementTool`
