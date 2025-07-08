# 📝 RESTful To-Do List API (Django + PostgreSQL + Docker)

A scalable REST API for managing to-do tasks, built with **Django REST Framework** and **PostgreSQL** — now fully **Dockerized** 🐳.  
This project is designed as a backend service that supports full CRUD operations on tasks. Ideal for practicing REST principles, authentication, and integrating with frontend frameworks like React or Vue.

---

## 🔧 Features

* ✅ Create / Read / Update / Delete Tasks  
* 🔐 JWT Authentication for securing endpoints  
* 🗂 Organized project structure  
* 🌱 PostgreSQL as the database  
* 🐳 Dockerized with `docker-compose`  
* ⚙️ Easily extendable for more features  

---

## 🚀 Getting Started (Without Docker)

1.  **Clone the repo**

    ```bash
    git clone https://github.com/nikanmafakheri/RESTful-ToDoList-django-postgres.git
    cd RESTful-ToDoList-django-postgres
    ```

2.  **Create virtual environment and activate it**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup PostgreSQL database**

    Make sure PostgreSQL is installed and running. Then create a new database and update the `DATABASES` section in `todolist/settings.py` with your credentials:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5.  **Apply migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Run the development server**

    ```bash
    python manage.py runserver
    ```

    Server will be available at: `http://127.0.0.1:8000/`

---

## 🐳 Getting Started with Docker

1.  **Make sure Docker and Docker Compose are installed**

2.  **Run the project with Docker Compose**

    ```bash
    sudo docker compose up --build
    ```

    This will build and run both the **Django app** and **PostgreSQL database** in containers.  
    Access the app at: `http://localhost:8000/`

---

## 📬 API Endpoints

| Method   | Endpoint           | Description                                        | Authentication Required |
|:--------:|:-------------------|:--------------------------------------------------|:------------------------:|
| `POST`   | `/token/`          | Obtain JWT access and refresh tokens              | No                       |
| `POST`   | `/token/refresh/`  | Refresh an expired access token                   | No                       |
| `GET`    | `/tasks/`          | List all tasks                                    | Yes                      |
| `POST`   | `/tasks/`          | Create a new task                                 | Yes                      |
| `GET`    | `/tasks/<id>/`     | Retrieve a single task                            | Yes                      |
| `PUT`    | `/tasks/<id>/`     | Update a task                                     | Yes                      |
| `DELETE` | `/tasks/<id>/`     | Delete a task                                     | Yes                      |

---

## 🔐 Authentication

This API uses **JSON Web Token (JWT)** for authentication.

* To access protected endpoints (like `/tasks/`), you must first obtain an access token.
* Send a `POST` request to `/token/` with your user credentials (e.g., username and password) to receive a new access and refresh token.
* Include the **access token** in the `Authorization` header of subsequent requests as a Bearer token:

    ```
    Authorization: Bearer <your_access_token>
    ```

* If your access token expires, use the `/token/refresh/` endpoint with your refresh token to get a new access token.

---

## 📁 Project Structure

```

RESTful-ToDoList-django-postgres/
├── todolist/             # Main Django project settings
├── apis/                 # App with Task models, views, serializers
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 👨‍💻 Author

**Nikan Mafakheri**

* [LinkedIn](https://www.linkedin.com/in/nikanmafakheri)  
* [GitHub: @nikanmafakheri](https://github.com/nikanmafakheri)

---

## 📄 License

This project is open source and available under the **MIT License**.
