from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from wishapp.models import Machine, Borrowed
from wishapp.forms import MachineForm, BorrowedForm

def machine_list(request):
    u"""機器一覧を表示する"""
    machines = Machine.objects.all()
    return render(request,
                  'wishapp/machine_list.html',
                  {'machine': machines})

def machine_add(request):
    u"""機器情報を追加する"""
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
    u"""機器情報を編集する"""
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
    u"""機器情報を削除する"""
    return HttpResponse('機器情報の削除')


def borrowed_list(request):
    u"""借用物一覧を表示する"""
    borrowed = Borrowed.objects.all()
    return render(request,
                  'wishapp/borrowed_list.html',
                  {'borrowed': borrowed})

def borrowed_add(request):
    u"""借用物を追加する"""
    borrowed = Borrowed()

    if request.method == 'POST':
        form = BorrowedForm(request.POST, instance=borrowed)  # POSTされたrequestデータからフォーム生成
        if form.is_valid():  # バリデーション
            borrowed = form.save(commit=False)
            borrowed.save()
            return redirect('wishapp:borrowed_list')
    else:  # GET の時
        form = BorrowedForm(instance=borrowed)  # machineインスタンスからフォーム生成

    return render(request, 'wishapp/borrowed_add.html', dict(form=form))
