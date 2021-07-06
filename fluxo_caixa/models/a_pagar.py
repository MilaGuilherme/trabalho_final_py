
from django.db import models
from django.db.models.aggregates import Sum
from . import Categorias

PAGAMENTO_TIPOS = (
    ('CD','Débito'),
    ('CC','Crédito'),
    ('T','Transferência'),
    ('P','Depósito'),
    ('C','Cheque'),
    ('D','Dinheiro'),
    ('B','Boleto'))

class ContasPagarManager(models.Manager):
    
  def get_from_date_range(self,init_date,end_date):
    contasPagar = self.filter(due_date__range=[init_date, end_date])
    contasPagar = self.order_by('due_date')
    return contasPagar 

class ContasPagar(models.Model):
  due_date = models.DateField(null=True, blank=True)
  payment_date = models.DateField(null=True, blank=True)
  value = models.FloatField()
  description = models.CharField(max_length=140, null=True, blank=True)
  category = models.ForeignKey(Categorias, on_delete=models.CASCADE)
  payment_method = models.CharField(max_length=20, choices=PAGAMENTO_TIPOS, default='D')
  status = models.BooleanField(default='false')
  objects = ContasPagarManager()