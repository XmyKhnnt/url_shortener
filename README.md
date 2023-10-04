# Django URL Shortener

## Overview

The Django URL Shortener is a web application that allows users to shorten long URLs into shorter, more manageable links. This project demonstrates the use of Django and Django REST framework to create a simple URL shortening service.

## How It Works

### Components

- **Link Model**: The `Link` model stores information about the original long URL, a unique shortened prefix, and an expiration time for the link.

- **Serializer**: The `LinkSerializer` class serializes `Link` objects to and from JSON format. It also generates a unique shorten prefix when creating a new link.

- **API Views**: The `LinkListCreateView` is an APIView that provides two endpoints: one for creating new shortened links via POST requests and another for retrieving a list of all shortened links via GET requests.

- **Redirection View**: The `redirect_to_original_url` view redirects users to the original long URL when they access a shortened link.

# Django URL Shortener

## How to Run

### Access the Application

- The server will start, and you can access the application at [http://localhost:8000/](http://localhost:8000/).

## API Endpoints

### Create a New Shortened Link

- Endpoint: POST [http://localhost:8000/links/](http://localhost:8000/links/)
- Instructions:
  - Send a JSON request with the `links` field containing the original URL.
- Response:
  - The API will respond with a JSON object containing the `shorten_prefix` and the complete URL.

### Retrieve All Shortened Links

- Endpoint: GET [http://localhost:8000/links/](http://localhost:8000/links/)

## Redirect to Original URL

- To access a shortened link, use the `shorten_prefix` as a path parameter, e.g., [http://localhost:8000/abcdef](http://localhost:8000/abcdef).
- If the link exists and has not expired, it will redirect you to the original URL. Otherwise, it will return a 404 error.

### Prerequisites

- Python 3.x
- Django
- Django REST framework

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/XmyKhnnt/url_shortener.git

   ```

   ```bash
   cd django-url-shortener

   ```

   ```bash
    python -m venv venv

   ```

   ```bash
   source venv/bin/activate

   ```

   ```bash
   .\venv\Scripts\activate

   ```

   ```bash
    pip install -r requirements.txt

   ```

### Database Setup

```bash
 python manage.py makemigrations

```

```bash
 python manage.py migrate

```

```bash
python manage.py runserver

```
