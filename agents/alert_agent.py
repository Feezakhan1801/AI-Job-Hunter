from apscheduler.schedulers.background import BackgroundScheduler

def send_daily_alert():
    print("Daily Jobs Sent!")

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_alert,'interval',hours=24)
scheduler.start()