from django.shortcuts import render
from django.http import Http404
from datetime import datetime, timedelta
from django.utils import timezone
from .models import QecData, QtaData, QscData

# def monitoring_dashboard(request):
#     # Your existing logic to gather monitoring data
#     monitoring_data = {
#         # Example data
#         'cpu_usage': '55%',
#         'ram_usage': '68%',
#         # Add more monitoring data as needed
#     }

#     # Include 'show_navbar': True in the context
#     context = {
#         'data': monitoring_data,
#         'show_navbar': True,  # This will show the navbar on the dashboard
#     }
    
#     return render(request, 'th_monitoring/dashboard.html', context)


def monitoring_dashboard(request):
    # Mapping of categories to their respective models
    model_mapping = {
        'qec': QecData,
        'qta': QtaData,
        'qsc': QscData,
    }
    
    latest_data = {}
    
    for category, model in model_mapping.items():
        # Adjusting the order_by to use 'date' and 'time' fields
        latest_entry = model.objects.all().order_by('-date', '-time').first()
        if latest_entry:
            latest_data[category] = {
                'date': latest_entry.date,
                'time': latest_entry.time,
                'temperature': latest_entry.temperature,
                'humidity': latest_entry.humidity,
            }
        else:
            latest_data[category] = 'No data available'
    
    context = {'latest_data': latest_data}
    print('latest_data', context)
    return render(request, 'latest_data.html', context)

