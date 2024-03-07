from django.apps import AppConfig


# The parameter 'verbose_name' is used to set a public name of our project
class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'
