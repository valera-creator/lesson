import schedule


def print_message(text):
    global i
    print(f"{i} {text}")
    i += 1
    if i == 5:
        return schedule.CancelJob


i = 0
schedule.every(1).seconds.do(print_message, text='ку-ку...')

while True:
    schedule.run_pending()







# второй способ
# def print_message(text):
#     global i
#     print(f"{i} {text}")
#     i += 1
#
#
# i = 0
# schedule.every(1).seconds.do(print_message, text='ку-ку...')
#
# while True:
#     schedule.run_pending()
#     if i == 5:
#         break






# def job():
#     print('я тута')
#
#
# schedule.every().monday.at("17:15:10").do(job)
# while True:
#     schedule.run_pending()
