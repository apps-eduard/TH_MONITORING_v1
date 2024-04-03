from apscheduler.schedulers.background import BackgroundScheduler
from .firebase import get_data_from_firebase
from .models import QecData, QtaData, QscData
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import math  # Import the math module

def send_email_alert(temperature, humidity, database_key):
    sender_email = "th.mon.sys@gmail.com"
    receiver_email = "th.mon.sys@gmail.com"
    password = "ofuf rziq tehc buxq"  # Consider using environment variables for security
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Alert: Temperature/Humidity Out of Range"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Convert database_key to uppercase for the email body
    database_key_upper = database_key.upper()
    
    text = f"""\
    Hi,
    An alert condition was detected in the {database_key_upper} Server Room !!!
    Temperature: {temperature}
    Humidity: {humidity}
    Please check the server of {database_key_upper}."""
    
    part = MIMEText(text, "plain")
    message.attach(part)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def fetch_and_save_data():
    model_mapping = {
        'qec': QecData,
        'qsc': QscData,
        'qta': QtaData,
    }
    
    for database_key in ['qec', 'qsc', 'qta']:
        data = get_data_from_firebase(database_key)
        for key, value in data.items():
            
            # Check if temperature or humidity is NaN and replace with 0.0
            temperature = float(value['temperature']) if not math.isnan(float(value['temperature'])) else 0.0
            humidity = float(value['humidity']) if not math.isnan(float(value['humidity'])) else 0.0
            
            # Save the data as before
            model = model_mapping.get(database_key)
            if model:
                model.objects.create(
                    date=datetime.datetime.strptime(value['date'], "%Y-%m-%d").date(),
                    time=datetime.datetime.strptime(value['time'], "%H:%M:%S").time(),
                    temperature=temperature,
                    humidity=humidity
                )

            # Send an email if the conditions are met
            if (temperature > 30 or temperature < 10) or (humidity > 80 or humidity < 15):
                send_email_alert(temperature, humidity, database_key)

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_save_data, 'interval', seconds=6000)  # Adjusted back to a more reasonable interval
    scheduler.start()
