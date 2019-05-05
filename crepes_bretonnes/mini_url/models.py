from django.db import models
from django.utils import timezone
import random
import string

class MiniURL(models.Model):
    url = models.URLField(unique=True, verbose_name="URL à réduire")
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    pseudo = models.CharField(max_length=100)
    acces = models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")

    class Meta:
        verbose_name="Mini URL"
        verbose_name_plural="Minis URL"

    def __str__(self):
        return "[{0}] {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generer(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        self.code = ''.join(aleatoire)