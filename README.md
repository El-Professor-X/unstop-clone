# 🎯 Unstop Clone – Hackathons & Competitions Platform

This is a full-stack clone of [Unstop.com](https://unstop.com) built using **Django + MySQL + Bootstrap**. It allows users to browse, register for, and organize events like hackathons, quizzes, internships, and hiring challenges.

## 🚀 Features

- ✅ User registration/login with Django auth
- ✅ JWT authentication (API ready)
- ✅ Event listing with filters (live, past, upcoming)
- ✅ Search bar for events
- ✅ Event detail and registration
- ✅ Organizer dashboard (Create/Edit/Delete events)
- ✅ Admin panel
- ✅ Image upload for events
- ✅ Mobile responsive (Bootstrap)
- ✅ Hosted on [Render](https://render.com)

## 🛠️ Tech Stack

- Python 3.11
- Django 5.x
- MySQL
- Bootstrap 5
- JWT (djangorestframework-simplejwt)

## 📸 Screenshots

| Homepage | Event Detail | Dashboard |
|----------|---------------|------------|
| ![home](screenshots/home.png) | ![detail](screenshots/detail.png) | ![dashboard](screenshots/dashboard.png) |

## 🧪 Run Locally

```bash
git clone https://github.com/your-username/unstop-clone.git
cd unstop-clone
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
