from fluxo_caixa.models import ContasPagar, ContasReceber
from fluxo_caixa.models.a_receber import RECEITA_TIPOS
from fluxo_caixa.models.a_pagar import PAGAMENTO_TIPOS
import datetime
import math
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.template.defaulttags import register
from fluxo_caixa.models import Categorias

MESES = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
         'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
saldo = 0

@csrf_exempt
@require_http_methods(['GET'])
def fluxo(request: HttpRequest):
    categorias = Categorias.objects.all()

    if request.method == 'GET':
        data = request.GET
        saldo = data.get('balance')
        init_date = data.get('end_date') if 'end_date' in request.GET else datetime.date.today(
        ).replace(month=1).isoformat()
        end_date = data.get(
            'init_date') if 'init_date' in request.GET else datetime.date.today().isoformat()

        mes1 = int(init_date.split('-',3)[1])
        mes2 = int(end_date.split('-',3)[1])

        meses = MESES[mes1:mes2] if mes1 < mes2 else [MESES[mes1-1]]

        contasPagar = ContasPagar.objects.get_from_date_range(init_date, end_date)
        contasReceber = ContasReceber.objects.get_from_date_range(init_date, end_date)

        pagamentos_mes = {'Jan':0, 'Fev':0, 'Mar':0, 'Abr':0, 'Mai':0, 'Jun':0,
         'Jul':0, 'Ago':0, 'Set':0, 'Out':0, 'Nov':0, 'Dez':0}

        recebimentos_mes = {'Jan':0, 'Fev':0, 'Mar':0, 'Abr':0, 'Mai':0, 'Jun':0,
         'Jul':0, 'Ago':0, 'Set':0, 'Out':0, 'Nov':0, 'Dez':0}

        for contas in contasPagar:
          conta_mes = get_month(contas.due_date)
          valor_mes = contas.value
          pagamentos_mes[conta_mes]+=valor_mes

        for contas in contasReceber:
          conta_mes = get_month(contas.due_date)
          valor_mes = contas.value
          recebimentos_mes[conta_mes]+=valor_mes

        result = {
            "Pagar": contasPagar,
            "Receber": contasReceber
        }

        print(recebimentos_mes)

        return render(request, 'fluxo.html', {'result': result, 'saldo': saldo, 'receita_tipos': dict(RECEITA_TIPOS), 'pagamento_tipos': dict(PAGAMENTO_TIPOS), 'categorias': categorias, 'meses':meses,'pagamentos_mes':pagamentos_mes, 'recebimentos_mes':recebimentos_mes})


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def round_num(value):
    return round(value,2)

@register.filter
def get_month(date):
  month = date.month
  month = MESES[month-1]
  return month
  
