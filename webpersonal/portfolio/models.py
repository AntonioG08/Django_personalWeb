from django.db import models


"""When creating a model for an app, 2 commands are esential here:
   python manage.py makemigrations 'app name'   and 
   python manage.py migrate 'app name'  """


# Create your models here (this will connect us to the DB)
class project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(max_length=300, verbose_name="Descripción")
    # The variable 'upload_to' allows us to save the images in a separate folder and keep everything organized
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Direccion web", null=True, blank=True)
    # With this, the register saves the date when its created. By default, Django hides this to avoid modifications
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    # With this, the register saves the date when its updated. By default, Django hides this to avoid modifications
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima modificación")

    # This class is used to change the public name of the model in the 'admin' section
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]  # puting a '-' indicates to go from newer to older

    # With this function we request to show the title as the public name, instead of a generic project name
    def __str__(self):
        return self.title
