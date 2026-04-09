# 🚀 REST_FRAMEWORK – Django REST Full-Stack App

REST_FRAMEWORK is a **full-stack Django + Django REST Framework application** that demonstrates **custom user management, API development, and dynamic frontend integration**.

It is built as a **portfolio-ready project** showcasing real-world backend concepts like **nested serializers, CRUD APIs, and frontend API consumption using JavaScript**.

---

## ✨ Features

### 🔐 Authentication & Users

* Custom User Model
* User Registration & Login
* Profile Page with Avatar
* Edit & Delete Profile
* Account Settings

---

### 🧩 Core Functionality

* Modular Django Architecture (Apps-based)
* Clean project structure
* Reusable templates & layouts
* Static file management

---

### 🌐 API & Backend (DRF)

* Django REST Framework integration
* Nested Serializers (User inside Comment)
* Full CRUD API for Comments:

  * ✅ Create Comment
  * ✅ Read Comments
  * ✅ Update Comment
  * ✅ Delete Comment
* API endpoints for profiles & comments
* JSON-based communication

---

### 💬 Comment System (Core Feature)

* Add comment with user selection
* Edit comment dynamically
* Delete comment with confirmation
* Real-time UI update after actions

---

### 🎨 Frontend (Dynamic UI)

* Built using **HTML + CSS + JavaScript**
* Fetch API for backend communication
* Black & white minimal UI design
* Responsive layout
* Clean typography and card-based UI

---

## 🔗 API Endpoints

### Profiles

```http
GET /api/profiles/
```

### Comments

```http
GET    /api/comments/
POST   /api/comments/add/
PATCH  /api/comments/<id>/edit/
DELETE /api/comments/<id>/delete/
```

---

## 🛠️ Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Frontend

* HTML
* CSS
* JavaScript (Fetch API)

### Database

* SQLite

### Tools

* Git & GitHub
* Virtual Environment (venv / uv)

---

## 📂 Project Structure

```bash
REST_FRAMEWORK/
│
├── _core/         # Main project config (settings, urls)
├── a_api/         # DRF API (views, serializers, urls)
├── a_home/        # Frontend views & templates
├── a_users/       # Custom user model & profile logic
├── static/        # CSS, images, assets
├── templates/     # HTML templates
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
# Clone repo
git clone https://github.com/your-username/REST_FRAMEWORK.git
cd REST_FRAMEWORK

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 📸 Demo

👉 Open in browser:

```bash
http://127.0.0.1:8000/frontend/
```

* View profiles
* Add comment
* Edit comment
* Delete comment

---

## 🚀 Future Improvements

* 🔐 Authentication-based permissions (only author can edit/delete)
* 🔍 Search & filtering
* 📄 Pagination
* 🌍 Deployment (Render / Railway)
* 📱 Mobile UI optimization

---

## 💡 What This Project Demonstrates

* Django app architecture
* REST API design with DRF
* Nested serializers
* Full CRUD operations
* Frontend ↔ Backend integration
* Clean UI design principles

---

## 👨‍💻 Author

**Surya Prakash Yadav**

---

## ⭐ If you like this project, give it a star on GitHub!