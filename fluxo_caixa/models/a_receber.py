from django.db import models
import datetime
from . import Categorias

RECEITA_TIPOS = (
    ('CD','Débito'),
    ('CC','Crédito'),
    ('T','Transferência'),
    ('P','Depósito'),
    ('C','Cheque'),
    ('D','Dinheiro'),
    ('B','Boleto'))

class ContasReceberManager(models.Manager):

  def get_from_date_range(self,init_date,end_date):
    contasReceber = self.filter(due_date__range=[init_date, end_date])
    contasReceber = self.order_by('due_date')
    return contasReceber

class ContasReceber(models.Model):
  due_date = models.DateField()
  value = models.FloatField()
  description = models.CharField(max_length=140, null=True, blank=True)
  category = models.ForeignKey(Categorias, on_delete=models.CASCADE)
  payment_method = models.CharField(max_length=20, choices=RECEITA_TIPOS, default='D')
  status = models.BooleanField(default='false')
  objects = ContasReceberManager()