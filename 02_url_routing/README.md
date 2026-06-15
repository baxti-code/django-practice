# 02 - URL Routing

Learning URL routing basics in Django.

## Topics Covered
- Static URLs (`/about/`, `/contact/`)
- Dynamic URLs (`/user/<str:username>/`)
- Integer URLs (`/post/<int:id>/`)

## Getting Started

```bash
python manage.py runserver
```

## URL Patterns

| URL | Description |
|---|---|
| `/` | Home page |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/user/<username>/` | User profile |
| `/post/<id>/` | Post detail |