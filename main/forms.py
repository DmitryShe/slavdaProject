from django import forms


class HotelsFilterForm(forms.Form):
    hostelType = forms.ChoiceField(help_text="Выбор типа отеля")
    price = forms.ChoiceField(help_text="Выбор цены")