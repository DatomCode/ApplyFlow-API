# 🚀 ApplyFlow API (Job Application Tracker)

A powerful RESTful API built with **Django** and **Django REST Framework (DRF)** to help job seekers organize their job search. This tool allows users to track applications, manage interview statuses, and keep detailed notes on every interaction.


## 📖 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Database Schema (ERD)](#-database-schema-erd)
- [Getting Started](#-getting-started)
- [API Endpoints](#-api-endpoints)
- [Future Improvements](#-future-improvements)


## ✨ Features

* **User Authentication:** Secure registration and login (Token/Session based).
* **CRUD Operations:** Create, Read, Update, and Delete job applications.
* **Status Tracking:** Move applications through stages (Applied → Interviewing → Offer).
* **Notes System:** Add multiple notes to specific job applications (e.g., recruiter feedback).
* **Data Validation:** Ensures data integrity (e.g., valid URLs, required fields).



## 🛠 Tech Stack

* **Language:** Python 3.x
* **Framework:** Django 5.x
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Authentication:** JWT / Token Authentication



## 📊 Database Schema (ERD)

The database consists of three main entities: **Users**, **Job Applications**, and **Interaction Notes**.

ER Diagram :(https://drive.google.com/file/d/1I0wcaV_j4s-tDD_u-n2JzU67pqdFvKey/view?usp=drive_link)




## 🚀 Getting Started

Follow these steps to set up the project locally on your machine.

### Prerequisites
* Python 3.8 or higher installed.
* Git installed.

### Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/careerquest-api.git](https://github.com/yourusername/careerquest-api.git)
    cd careerquest-api
    ```

2.  **Create a Virtual Environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Start the Development Server**
    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000/` in your browser to verify it's running!



## 📡 API Endpoints

### 🔐 Authentication
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Login and get token |

### 💼 Job Applications
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/jobs/` | List all job applications |
| `POST` | `/api/jobs/` | Create a new application |
| `GET` | `/api/jobs/<id>/` | Get details of one job |
| `PUT` | `/api/jobs/<id>/` | Update job details |
| `DELETE` | `/api/jobs/<id>/` | Delete a job application |

### 📝 Notes
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/jobs/<id>/notes/` | Get notes for a specific job |
| `POST` | `/api/jobs/<id>/notes/` | Create a note for a specific job |



## 🔮 Future Improvements
* Add filtering by job status (e.g., `?status=Interviewing`).
* Integrate an external API to fetch real job listings.
* Email notifications for upcoming interviews.



## 👤 Author
**Gbadebo Enoch**
- LinkedIn: https://www.linkedin.com/in/gbadeboenoch/
- GitHub: https://github.com/DatomCode
