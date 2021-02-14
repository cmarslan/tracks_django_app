from django import forms


class DatePicker(forms.Form):
    period_start = forms.DateField(initial='2020-10-01', required=True)
    period_end = forms.DateField(initial='2030-01-01', required=True)
    start_cities = (
        ('Berlin', 'Berlin'), ('Hamburg', 'Hamburg'), ('München', 'München'))
    start_city = forms.MultipleChoiceField(choices=start_cities, widget=forms.CheckboxSelectMultiple, required=True)
    end_cities = (
        ('Berlin', 'Berlin'), ('Hamburg', 'Hamburg'), ('München', 'München'), ('Bremen', 'Bremen'))
    end_city = forms.MultipleChoiceField(choices=end_cities, widget=forms.CheckboxSelectMultiple, required=True)
    type_of_calculation_choices = (
        ('primary', 'Primary'), ('modeled', 'Modeled'), ('default', 'Default')
    )
    type_of_calculation = forms.MultipleChoiceField(choices=type_of_calculation_choices,
                                                    widget=forms.CheckboxSelectMultiple, required=True)
    type_of_goods_choices = (
        ('Container', 'Container'), ('Chemicals', 'Chemicals'), ('Cereals', 'Cereals')
    )
    type_of_goods = forms.MultipleChoiceField(choices=type_of_goods_choices, widget=forms.CheckboxSelectMultiple,
                                              required=True)
