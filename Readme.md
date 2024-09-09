# Gurkha Geeks

Gurkha Geeks is an open-source project aimed at bringing together all tech enthusiasts from Nepal. This platform allows developers, designers, and other tech-minded individuals to collaborate on various projects, share knowledge, and contribute to the growing tech community in Nepal.

## Table of Contents

- [About the Project](#about-the-project)
- [Installation](#installation)
  - [Backend Setup (Django REST Framework)](#backend-setup-django-rest-framework)
- [Usage](#usage)
- [Contributing](#contributing)

## About the Project

Gurkha Geeks is designed to be a collaborative platform where tech enthusiasts of Nepal can contribute, learn, and grow together. Whether you're a developer, designer, or just someone interested in tech, you're welcome to contribute to this repository. The project is built with Django REST Framework for the backend and React for the frontend, making it a versatile and scalable application.

## Installation

To set up the project locally, follow these steps:

### Backend Setup (Django REST Framework)

1. **Clone the repository**

   ```bash
   git clone https://github.com/Kushaldotel/gurkhageeks
   cd gurkha-geeks/backend

2. **Create a virtual environment**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt

4. **Set up the database**

    ```bash
    python manage.py migrate

5. Run the development server

    ```bash
    python manage.py runserver


### Usage
Once the project is set up, you can start contributing to either the frontend or backend. The backend server will run on http://localhost:8000/. The backend API endpoints will be accessible via the Django REST Framework interface.


### Contributing
We welcome contributions from all tech enthusiasts! Whether you're a seasoned developer or just starting, your contributions are valuable.

To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/your-feature-name).
3. Make your changes and commit them (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature/your-feature-name).
5. Open a Pull Request.
6. Please ensure that your contributions adhere to our Code of Conduct.
