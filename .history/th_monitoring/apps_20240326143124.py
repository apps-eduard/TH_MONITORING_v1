from django.apps import AppConfig

class ThMonitoringConfig(AppConfig):
    name = 'th_monitoring'

    def ready(self):
        from . import tasks
        tasks.start()