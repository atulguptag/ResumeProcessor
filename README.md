# ResumeProcessor

## Project Overview

ResumeProcessor is a Django-based web application that provides a REST API endpoint to process resumes and extract the candidate's first name, email ID, and mobile number. The extracted information is stored in a PostgreSQL database.

## Features

- Upload resume files (PDF or Word documents)
- Extract candidate's first name, email ID, and mobile number
- Store extracted information in a PostgreSQL database
- REST API endpoint for resume processing

## Requirements

- Python 3.9 or later
- Django 5.x or later
- PostgreSQL
- Django REST Framework
- pyresparser
- spaCy

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/atulguptag/ResumeProcessor.git
cd ResumeProcessor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment.
  - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
  - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure PostgreSQL Database

Update the `DATABASES` setting in `ResumeProcessor/settings.py` with your PostgreSQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name', # Database Name
        'USER': 'your_db_user', #Mostly, `postgres`
        'PASSWORD': 'your_db_password', # Database Password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Download spaCy Model

```bash
pip install -U spacy
python -m spacy download en_core_web_sm
```

### 8. Create Uploads Directory

```bash
mkdir uploads
```

### 9. Run the Development Server

```bash
python manage.py runserver
```

### 10. Test the API Endpoint

You can test the API endpoint using `Postman` or `curl`.

#### Using `Postman`

1. Create a new POST request.
2. Set the URL to `http://127.0.0.1:8000/api/extract_resume/`.
3. In the Body tab, select `form-data`.
4. Add a key named `resume` and set the type to `File`.
5. Choose the resume file to upload.
6. Click Send.

#### Using `curl`

```bash
curl -X POST http://127.0.0.1:8000/api/extract_resume/ -F "resume=@path/to/your/resume.pdf"
```

### Example Response

```json
{
  "first_name": "John",
  "email": "john.doe@example.com",
  "mobile_number": "123-456-7890"
}
```

## Project Structure

```
ResumeProcessor/
├── manage.py
├── ResumeProcessor/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── resume/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── uploads/
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [pyresparser](https://github.com/OmkarPathak/pyresparser)
- [spaCy](https://spacy.io/)

