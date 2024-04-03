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
