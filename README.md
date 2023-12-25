# Bigcorp Shop

## Description
Bigcorp Shop is a Django ecommerce project with an API and various features.
[this YouTube playlist](https://www.youtube.com/playlist?list=PLDJd4Vk8aVpGxeF2BS0s3rwmDrj3aEwwx)

## Installation
To run the project, follow these steps:
1. Build the project locally using Docker Compose: $sudo docker-compose build
2. Run the project: $ sudo docker-compose up

## Usage
1. After running the project, create a superuser using the following command: $ sudo docker exec -it bigcorp-backend python manage.py createsuperuser
2. Access the admin interface in your browser and manually create at least one category for products.
3. Generate fake products using the following command: $ sudo docker exec -it bigcorp-backend python manage.py fakeproducts

## Technologies Used
This project is built using the following technologies:
- Python
- JavaScript
- Ajax
- CSS
- HTML
- Postgres
- Celery Beat
- Celery Result
- Celery
- Redis Broker
- Django Htmx
- Nginx
- Gunicorn
- API
- Swagger and Redoc Docs
- Celery Flower
- Stripe
- Yookassa
- Django Rest Framework
- Docker
- Docker Compose
- GitHub Actions
- Git

## Future Improvements
This project is a work in progress and will be improved further.

## Contribution Guidelines
Contributions to this project are welcome. Please follow the standard contribution guidelines.

## Acknowledgements
Special thanks to for every supporter [this YouTube playlist](https://www.youtube.com/playlist?list=PLDJd4Vk8aVpGxeF2BS0s3rwmDrj3aEwwx) for providing motivation on creating this project.

## License
This project is open source.