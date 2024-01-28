import schedule


def print_message(text):
    global i
    print(f"{i} {text}")
    i += 1
    if i == 5:
        return schedule.CancelJob


i = 0
schedule.every(1).seconds.do(print_message, text='ку-ку...')

while True:  # цикл бесконечный
    schedule.run_pending()
