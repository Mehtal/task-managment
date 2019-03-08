from django import forms
from .models import Supply
from taskmanagment.models import Tool, Project, Area, Task


class RestockForm(forms.Form):
    name = forms.CharField(max_length="30")
    quantity = forms.IntegerField(min_value=0)
    unit_price = forms.DecimalField(max_digits=11, decimal_places=2)
    new_quantity = forms.IntegerField(min_value=0)
    new_price = forms.DecimalField(max_digits=11, decimal_places=2)


class SupplyForm(forms.ModelForm):
    new_quantity = forms.IntegerField(min_value=0)
    new_price = forms.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        model = Supply
        fields = ["name", "quantity", "unit_price", ]

    def clean(self):
        cleaned_data = super().clean()
        instance = self.instance
        old_supply = instance.quantity * instance.unit_price
        new_supply = cleaned_data.get('new_quantity') * cleaned_data.get('new_price')
        quantity = instance.quantity + cleaned_data.get('new_quantity')
        instance.unit_price = (old_supply + new_supply) / quantity
        instance.quantity = quantity
        instance.save()
        cleaned_data["quantity"] = round(instance.quantity, 2)
        cleaned_data["unit_price"] = round(instance.unit_price, 2)
        return cleaned_data

    def save(self, commit=True):
        instance = super(SupplyForm, self).save()
        # print("save method ------------>", instance.quantity,)
        return instance


def get_supply_list():
    supply_list = Supply.objects.all().iterator()
    return supply_list


class SendToTaskForm(forms.Form):

    project = forms.ModelChoiceField(queryset=Project.objects.all())
    area = forms.ModelChoiceField(queryset=Project.objects.all())
    task = forms.ModelChoiceField(queryset=Area.objects.all())
    name = forms.ModelChoiceField(queryset=Supply.objects.all())
    quantity = forms.IntegerField(min_value=0)

    def __init__(self, *args, **kwargs):
        super(SendToTaskForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = Supply.objects.all()
        self.fields['project'].queryset = Project.objects.all()
        self.fields['area'].queryset = Area.objects.none()
        self.fields['task'].queryset = Task.objects.none()

        if 'project' in self.data:
            try:
                project_id = int(self.data.get('project'))
                self.fields['area'].queryset = Area.objects.filter(project_id=project_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty area queryset
        if 'area' in self.data:
            try:
                area_id = int(self.data.get('area'))
                self.fields['task'].queryset = Task.objects.filter(area_id=area_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty area queryset
