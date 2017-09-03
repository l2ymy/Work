from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from wishapp.models import Machine
from wishapp.forms import MachineForm

def machine_list(request):
    """機器一覧"""
    machines = Machine.objects.all()
    return render(request,
                  'wishapp/machine_list.html',
                  {'machine': machines})

def machine_add(request):
    """機器情報の追加"""
    machine = Machine()

    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)  # POSTされたrequestデータからフォーム生成
        if form.is_valid():  # バリデーション
            machine = form.save(commit=False)
            machine.save()
            return redirect('wishapp:machine_list')
    else:  # GET の時
        form = MachineForm(instance=machine)  # machineインスタンスからフォーム生成

    return render(request, 'wishapp/machine_add.html', dict(form=form))

def machine_edit(request):
    """機器情報の編集"""
    if machine_id:
        machine = get_object_or_404(machine, pk=machine_id)
    else:
        machine = machine()

    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine)  # POSTされたrequestデータからフォーム生成
        if form.is_valid():  # バリデーション
            machine = form.save(commit=False)
            machine.save()
            return redirect('wishapp:machine_list')
    else:  # GET の時
        form = MachineForm(instance=machine)  # machineインスタンスからフォーム生成

    return render(request, 'wishapp/machine_edit.html', dict(form=form, machine_id=machine_id))

def machine_delete(request):
    """機器情報の削除"""
    return HttpResponse('機器情報の削除')
