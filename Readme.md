[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Discord][discord-shield]][discord-url]


# Gurkha Geeks

Gurkha Geeks is an open-source project aimed at bringing together all tech enthusiasts from Nepal. This platform allows developers, designers, and other tech-minded individuals to collaborate on various projects, share knowledge, and contribute to the growing tech community in Nepal.

## Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#teach-stack)
- [Installation](#installation)
  - [Backend Setup (Django REST Framework)](#backend-setup-django-rest-framework)
- [Usage](#usage)
- [Contributing](#contributing)

## About the Project

Gurkha Geeks is designed to be a collaborative platform where tech enthusiasts of Nepal can contribute, learn, and grow together. Whether you're a developer, designer, or just someone interested in tech, you're welcome to contribute to this repository. The project is built with Django REST Framework for the backend and React for the frontend, making it a versatile and scalable application.

## Tech Stack 
[![Django][Django]][Django-url] 
[![DRF][DRF]][DRF-url] 
[![React][React.js]][React-url] 
[![PostgreSQL][PostgreSQL]][Postgresql-url]

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

For detailed guidelines on how to contribute, please refer to our [Contribution Guidelines](CONTRIBUTING.md).

### Quick Overview

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'feat:Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.
6. Ensure that your contributions adhere to our Code of Conduct.

### Contributors

<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/kushaldotel"><img src="https://avatars.githubusercontent.com/u/114340617?v=4" width="100px;" alt="Kushal"/><br /><sub><b>Kushal</b></sub></a><br />
        <a href="#" title="Maintenance">🔧</a>
        <a href="#" title="Project Management">📆</a>
        <a href="#" title="Code">💻</a>
        <a href="#" title="Reviewed Pull Requests">👀</a>
        <a href="#" title="Ideas, Planning, & Feedback">🤔</a>
      </td>
      <td align="center" valign="top" width="14.28%">
        <a href="https://github.com/pawansapkota100"><img src="https://avatars.githubusercontent.com/u/100679210?s=96&v=4" width="100px;" alt="Pawan"/><br /><sub><b>Pawan</b></sub></a><br />
        <a href="#" title="Maintenance">🔧</a>
        <a href="#" title="Documentation">📖</a>
        <a href="#" title="Code">💻</a>
        <a href="#" title="Content">🖋</a>
        <a href="#" title="Ideas, Planning, & Feedback">🤔</a>
        </td>
    </tr>
  </tbody>
</table>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Kushaldotel/gurkhageeks.svg?style=for-the-badge
[contributors-url]: https://github.com/Kushaldotel/gurkhageeks/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Kushaldotel/gurkhageeks.svg?style=for-the-badge
[forks-url]: https://github.com/Kushaldotel/gurkhageeks/network/members
[stars-shield]: https://img.shields.io/github/stars/Kushaldotel/gurkhageeks.svg?style=for-the-badge
[stars-url]: https://github.com/Kushaldotel/gurkhageeks/stargazers
[issues-shield]: https://img.shields.io/github/issues/Kushaldotel/gurkhageeks.svg?style=for-the-badge
[issues-url]: https://github.com/Kushaldotel/gurkhageeks/issues
[license-shield]: https://img.shields.io/github/license/Kushaldotel/gurkhageeks.svg?style=for-the-badge
[license-url]: https://github.com/Kushaldotel/gurkhageeks/blob/main/LICENSE
[discord-shield]: https://img.shields.io/discord/your_discord_server_id.svg?style=for-the-badge
[discord-url]: https://discord.gg/CVNrjK3gpB
[Django]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[DRF]: https://img.shields.io/badge/DRF-092E20?style=for-the-badge&logo=django&logoColor=red
[DRF-url]: https://www.django-rest-framework.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[PostgreSQL]: https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white
[Postgresql-url]: https://www.postgresql.org/

