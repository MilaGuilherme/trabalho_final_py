from fluxo_caixa.models.categorias import CATEGORIA_TIPOS
from fluxo_caixa.models import Categorias
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.template.defaulttags import register


@csrf_exempt
@require_http_methods(['GET','POST'])
def categorias(request):  
  if request.method == 'POST':
    data = request.POST
    categoria = Categorias()
    categoria.name = data['name']
    categoria.description = data['description']
    categoria.category_type = data['category_type']
    categoria.save()
    return HttpResponseRedirect('/categorias')

  return render(request, 'categorias.html', { 'categorias': Categorias.objects.all(), 'cat_type':dict(CATEGORIA_TIPOS)})


@csrf_exempt
@require_http_methods(['POST'])
def delete_categorias(request,id):
  if request.method == 'POST':
    Categorias.objects.filter(id=id).delete()
    return HttpResponseRedirect('/categorias')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)