from django.apps import AppConfig


class CatsConfig(AppConfig):
    default_cat_field = 'django.db.models.BigCatsField'
    name = 'cats'
