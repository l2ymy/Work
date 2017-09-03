from django.forms import ModelForm
from wishapp.models import Machine 


class MachineForm(ModelForm):
    """検証機器登録フォーム"""
    class Meta:
        model = Machine
        fields = ('author', 'vender', 'name', 'cpuinfo', 'meminfo',
                  'nicinfo', 'biosinfo')
