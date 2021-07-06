from fluxo_caixa.models.categorias import Categorias
from fluxo_caixa.models.a_pagar import ContasPagar
from django.http.request import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponseRedirect


@csrf_exempt
@require_http_methods(['POST'])
def criar_a_pagar(request: HttpRequest):
  if request.method == 'POST':
    data = request.POST
    conta = ContasPagar()
    conta.due_date = data.get('due_date')
    conta.payment_date = data.get('payment_date')
    conta.value = data.get('value')
    conta.description = data.get('description')
    conta.category = Categorias.objects.get(id=data.get('category'))
    conta.payment_method = data.get('payment_method')
    conta.status = True if data.get('status') == "True" else False
    conta.save()

    return HttpResponseRedirect('/')