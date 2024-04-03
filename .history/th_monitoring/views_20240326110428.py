from django.shortcuts import render

# Example of a simple monitoring view
def monitoring_dashboard(request):
    # In a real scenario, you would query your database or monitoring service here
    # For demonstration, we'll use static data
    monitoring_data = {
        'cpu_usage': '55%',
        'ram_usage': '68%',
        'disk_space': '87%',
        'network_status': 'Good',
        'number_of_active_users': 120,
    }
    
    return render(request, 'th_monitoring/dashboard.html', {'data': monitoring_data})
