from django.forms import ModelForm
from wishapp.models import Machine, Borrowed


class MachineForm(ModelForm):
    """検証機器登録フォーム"""
    class Meta:
        model = Machine
        fields = ('author', 'vender', 'name', 'cpuinfo', 'meminfo',
                  'nicinfo', 'biosinfo')


class BorrowedForm(ModelForm):
    """借用物登録フォーム"""
    class Meta:
        model = Borrowed
        fields = ('borrow_personnel', 'borrow_date', 'borrow_check', 'return_date')
