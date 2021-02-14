from django.shortcuts import render

from .forms import DatePicker
from .models import Shipments


def tracks_emission(request):
    sort_column = request.GET.get('sort_by', 'start_city')
    all_data = Shipments.objects.all().order_by(sort_column)
    if request.method == 'POST':
        form = DatePicker(request.POST)
        if form.is_valid():
            period_start = form.cleaned_data['period_start']
            period_end = form.cleaned_data['period_end']
            all_data = Shipments.objects.filter(
                start_time__gte=period_start,
                end_time__lte=period_end).filter(
                start_city__in=form.cleaned_data['start_city']).filter(
                end_city__in=form.cleaned_data['end_city']).filter(
                type_of_calculations__in=form.cleaned_data['type_of_calculation']).filter(
                type_of_goods__in=form.cleaned_data['type_of_goods']).order_by(sort_column)
    else:
        form = DatePicker
    context = {
        'form': form,
        'all_data': all_data,
    }
    return render(request, "emissions.html", context)
