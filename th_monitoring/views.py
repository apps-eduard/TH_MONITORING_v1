from django.shortcuts import render, redirect
from django.http import Http404
from datetime import datetime, timedelta
from django.utils import timezone
from .models import QecData, QtaData, QscData
from .forms import EmailSettingsForm
from django.core.exceptions import ObjectDoesNotExist

def dashboard_view(request):
    # Mapping of categories to their respective models
    model_mapping = {
        'qec': QecData,
        'qta': QtaData,
        'qsc': QscData,
    }
    
    latest_data = {}
    
    for category, model in model_mapping.items():
        try:
            # Attempt to get the latest entry by the highest ID
            latest_entry = model.objects.latest('id')
            
            # If successful, store the relevant data in the dictionary
            latest_data[category] = {
                'date': latest_entry.date,
                'time': latest_entry.time,
                'temperature': latest_entry.temperature,
                'humidity': latest_entry.humidity,
            }
        except ObjectDoesNotExist:
            # Handle the case where no entries exist for the model
            latest_data[category] = 'No data available'
    
    context = {'latest_data': latest_data, 'show_navbar': True}
    
    return render(request, 'th_monitoring/dashboard.html', context)


def trend_page(request):
    # Category mapping to model classes
    model_map = {
        'qec': QecData,
        'qta': QtaData,
        'qsc': QscData,
    }
    
    # Calculate dates for the last month
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=30)
    
    # Format dates for the input fields
    default_end_date = end_date.strftime('%Y-%m-%d')
    default_start_date = start_date.strftime('%Y-%m-%d')
    
    # Get category and dates from GET request or use defaults
    category = request.GET.get('category', 'qsc').lower()  # Default to 'qsc' if not provided
    selected_start_date = request.GET.get('start_date', default_start_date)
    selected_end_date = request.GET.get('end_date', default_end_date)

    # Validate category
    if category not in model_map:
        return render(request, 'error_page.html', {'error': 'Invalid category specified'})

    # Get the model based on the category
    model = model_map[category]

    # Fetch data from the model based on the selected date range
    data = model.objects.filter(
        date__gte=selected_start_date,
        date__lte=selected_end_date
    ).order_by('-date', '-time')

    context = {
        'category': category.upper(),
        'data': data,
        'start_date': selected_start_date,
        'end_date': selected_end_date,
        'show_navbar': True
    }

    return render(request, 'th_monitoring/trend_page.html', context)

def email_settings(request):
    if request.method == "POST":
        form = EmailSettingsForm(request.POST)
        if form.is_valid():
            form.save()
            # Ensure you have a URL named 'success_url' defined in your urls.py, or change this to an appropriate redirect.
            return redirect('th_monitoring:dashboard')  # Example: redirecting to the dashboard after saving.
    else:
        form = EmailSettingsForm()
    
    # Adjusted the template path to include the app name as a namespace.
    return render(request, 'th_monitoring/email_settings.html', {'form': form, 'show_navbar': True})
