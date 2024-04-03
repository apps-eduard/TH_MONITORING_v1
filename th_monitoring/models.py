from django.db import models

class BaseMonitoringData(models.Model):
    date = models.DateField()
    time = models.TimeField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        abstract = True  # This makes the model abstract, so it won't create a separate table

class QecData(BaseMonitoringData):
    pass  # Inherits everything from BaseMonitoringData

    def __str__(self):
        return f"QEC data on {self.date} at {self.time}"

class QtaData(BaseMonitoringData):
    pass  # Inherits everything from BaseMonitoringData

    def __str__(self):
        return f"QTA data on {self.date} at {self.time}"

class QscData(BaseMonitoringData):
    pass  # Inherits everything from BaseMonitoringData

    def __str__(self):
        return f"QSC data on {self.date} at {self.time}"


class EmailSettings(models.Model):
    sender_email = models.EmailField(max_length=254)
    receiver_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)  # Consider encrypting this field for security

    def __str__(self):
        return "Email Settings"







