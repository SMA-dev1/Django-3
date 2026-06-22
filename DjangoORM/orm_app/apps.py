from django.apps import AppConfig


class OrmAppConfig(AppConfig):
    name = 'orm_app'
    default_auto_field = 'django.db.models.BigAutoField'
