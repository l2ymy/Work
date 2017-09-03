from django.shortcuts import render
from django.http import HttpResponse

from wishapp.models import Machinery

def machinery_list(request):
    """機器一覧"""
    machinery = Machinery.objects.all().order_by('id')
    return render(request,
                  'wishapp/machinery_list.html',  # 使用するテンプレート
                  {'machinery': machinery})  # テンプレートに渡すデータ

def machinery_add(request):
    """機器情報の追加"""
    return HttpResponse('機器情報の追加')

def machinery_edit(request):
    """機器情報の編集"""
    return HttpResponse('機器情報の編集')

def machinery_del(request):
    """機器情報の削除"""
    return HttpResponse('機器情報の削除')
