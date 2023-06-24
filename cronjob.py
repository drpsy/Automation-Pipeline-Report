from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from automation_mail import main_auto_mail, history_auto_mail
from database_dump import main_componentdb_dump
from gmail_attach import main_gmail_attachments

def execute():
    print(f"Crawling at {datetime.now()}.")
    try: 
        main_gmail_attachments()
        main_gmail_attachments()
    except: 
        print("mail not found")
    

scheduler = BlockingScheduler()


#cronjob will be run at 13:00 and 15 every day
scheduler.add_job(
    func= execute, 
    trigger=CronTrigger.from_crontab(expr="00 13,14 * * *")
)
scheduler.add_job(
    func =  main_auto_mail, 
    trigger= CronTrigger.from_crontab(expr="00 14,15 * * *")
)
scheduler.add_job(
    func= history_auto_mail, 
    trigger=CronTrigger.from_crontab(expr="00 15,16 * * *"),

)

try: 
    execute()
except Exception as e: 
    print(e)

try: 
    main_auto_mail()
except Exception as e: 
    print(e)

scheduler.start()


