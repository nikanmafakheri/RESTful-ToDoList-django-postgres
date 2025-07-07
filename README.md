


# 📝 RESTful To-Do List API (Django + PostgreSQL)

A simple yet scalable REST API for managing to-do tasks, built with **Django REST Framework** and **PostgreSQL**.

This project is designed as a backend service that supports full CRUD operations on tasks. Ideal for practicing REST principles, authentication, and integrating with frontend frameworks like React or Vue.

---

## 🔧 Features

- ✅ Create / Read / Update / Delete Tasks
- 🔐 JWT Authentication (in progress)
- 🗂 Organized project structure
- 🌱 PostgreSQL as the database
- ⚙️ Easily extendable for more features

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/nikanmafakheri/RESTful-ToDoList-django-postgres.git
cd RESTful-ToDoList-django-postgres
````

### 2. Create virtual environment and activate it

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL database

Make sure PostgreSQL is installed and running. Then create a new database and update the `DATABASES` section in `todo/settings.py` with your credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Server will be available at: `http://127.0.0.1:8000/`

---

## 📬 API Endpoints

| Method | Endpoint     | Description            |
| ------ | ------------ | ---------------------- |
| GET    | /tasks/      | List all tasks         |
| POST   | /tasks/      | Create a new task      |
| GET    | /tasks/<id>/ | Retrieve a single task |
| PUT    | /tasks/<id>/ | Update a task          |
| DELETE | /tasks/<id>/ | Delete a task          |

---

## 🔐 Authentication (Coming Soon)

JWT-based authentication will be added soon to secure endpoints.

---

## 📁 Project Structure

```
RESTful-ToDoList-django-postgres/
├── todolist/             # Main Django project
├── apis/            # App with Task models, views, serializers
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 👨‍💻 Author

* Nikan Mafakheri
* [LinkedIn](https://www.linkedin.com/in/nikanmafakheri/)
* GitHub: [@nikanmafakheri](https://github.com/nikanmafakheri)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

```
