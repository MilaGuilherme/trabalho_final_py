from django.db import models

CATEGORIA_TIPOS = (
  ('S','Saídas'),
  ('E','Entradas'))
  
class Categorias(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=140, null=True, blank=True)
  category_type = models.CharField(max_length=20, choices=CATEGORIA_TIPOS, default='S')