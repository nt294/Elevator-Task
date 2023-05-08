from django import forms
from django.contrib import admin
from .models import Floor, Elevator, ControlPanel


class ElevatorAdminForm(forms.ModelForm):
    class Meta:
        model = Elevator
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['target_floor'].widget = forms.HiddenInput()
        self.fields['direction'].widget = forms.HiddenInput()



class ElevatorAdmin(admin.ModelAdmin):
    form = ElevatorAdminForm
    readonly_fields = ('id',)


class FloorAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class ControlPanelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Floor, FloorAdmin)
admin.site.register(Elevator, ElevatorAdmin)
admin.site.register(ControlPanel, ControlPanelAdmin)
