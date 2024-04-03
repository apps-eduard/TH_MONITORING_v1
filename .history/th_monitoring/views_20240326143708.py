from django.shortcuts import render

def monitoring_dashboard(request):
    # Your existing logic to gather monitoring data
    monitoring_data = {
        # Example data
        'cpu_usage': '55%',
        'ram_usage': '68%',
        # Add more monitoring data as needed
    }

    # Include 'show_navbar': True in the context
    context = {
        'data': monitoring_data,
        'show_navbar': True,  # This will show the navbar on the dashboard
    }
    
    return render(request, 'th_monitoring/dashboard.html', context)


def latest_data_view(request):
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
    }

    return render(request, 'trend_page.html', context)


