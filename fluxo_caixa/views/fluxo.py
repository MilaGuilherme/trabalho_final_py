from fluxo_caixa.models import ContasPagar, ContasReceber
from fluxo_caixa.models.a_receber import RECEITA_TIPOS
from fluxo_caixa.models.a_pagar import PAGAMENTO_TIPOS
import datetime
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.template.defaulttags import register
from fluxo_caixa.models import Categorias

MESES = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']


@csrf_exempt
@require_http_methods(['GET'])
def fluxo(request: HttpRequest):
    categorias = Categorias.objects.all()

    if request.method == 'GET':
        data = request.GET
        saldo = data.get('balance')
        init_date = data.get('end_date') if 'end_date' in request.POST else datetime.date.today(
        ).replace(month=1).isoformat()
        end_date = data.get(
            'init_date') if 'init_date' in request.POST else datetime.date.today().isoformat()

        mes1 = int(init_date.split('-',3)[1])
        mes2 = int(end_date.split('-',3)[1])
        meses = MESES[mes1:mes2]

        contasPagar = ContasPagar.objects.get_from_date_range(init_date, end_date)
        contasReceber = ContasReceber.objects.get_from_date_range(init_date, end_date)

        result = {
            "Pagar": contasPagar,
            "Receber": contasReceber
        }

        return render(request, 'fluxo.html', {'result': result, 'saldo': saldo, 'receita_tipos': dict(RECEITA_TIPOS), 'pagamento_tipos': dict(PAGAMENTO_TIPOS), 'categorias': categorias, 'meses':meses})


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def get_month(date):
  month = date.month
  month = MESES[month-1]
  return month
  
