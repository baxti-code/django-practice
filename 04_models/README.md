# 04 - Models

Learning Django Models and ORM (Object-Relational Mapping).

## Topics Covered
- Creating models (`models.py`)
- Migrations (`makemigrations`, `migrate`)
- Django Admin panel (`createsuperuser`, `admin.py`)
- ORM queries (`Post.objects.all()`)
- `get_object_or_404` for safe lookups
- List view and Detail view
- Linking between pages using `pk`

## Getting Started

```bash
python manage.py runserver
```

## Pages

| URL | Description |
|---|---|
| `/` | List of all blog posts |
| `/post/<int:pk>/` | Detail page for a single post |
| `/admin/` | Django admin panel |