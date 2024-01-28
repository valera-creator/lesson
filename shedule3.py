import schedule


def job():
    print('я тута')


schedule.every().monday.at("17:15:10").do(job)
while True:
    schedule.run_pending()
