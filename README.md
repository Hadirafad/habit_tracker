# 🧠 Django Habit Tracker API

Track your daily habits with JWT-secured RESTful APIs, complete with interactive Swagger documentation.

---

## 🚀 Features

- 🔐 JWT-based user authentication (access + refresh tokens)
- 📅 CRUD APIs for managing daily habits
- 📄 Auto-generated Swagger UI (`drf-yasg`)
- 💾 MySQL database integration
- ☁️ Deployable on Render, Railway, or any cloud platform

---

## 🛠️ Tech Stack

- **Language**: Python 3.10
- **Backend**: Django 4.x, Django REST Framework
- **Auth**: Simple JWT
- **Docs**: drf-yasg (Swagger)
- **Database**: MySQL
- **Hosting**: Render (or Railway, etc.)

---

## 🧑‍💻 Local Setup

1. **Clone the repo** : 
   git clone https://github.com/YOUR_USERNAME/habit_tracker.git
   cd habit_tracker

2. **Create & activate a virtual environment** : 
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

4. **Install dependencies**: 
   pip install -r requirements.txt

5. **create .env file** : 
   SECRET_KEY=your_django_secret
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_user
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306

6. **Apply migrations** : 
   python manage.py migrate

7. **Run the server** : 
     python manage.py runserver

