from django.shortcuts import render
from django.http import HttpResponse

from wishapp.models import Machine

def machine_list(request):
    """機器一覧"""
    machines = Machine.objects.all().order_by('id')
    return render(request,
                  'wishapp/machine_list.html',
                  {'machine': machines})

def machine_add(request):
    """機器情報の追加"""
    return HttpResponse('機器情報の追加')

def machine_edit(request):
    """機器情報の編集"""
    return HttpResponse('機器情報の編集')

def machine_del(request):
    """機器情報の削除"""
    return HttpResponse('機器情報の削除')
