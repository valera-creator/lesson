import schedule


# второй способ
def print_message2(text):
    global n
    print(f"{n} {text}")
    n += 1


n = 0
schedule.every(1).seconds.do(print_message2, text='ку-ку...')

while True:  # цикл завершится
    schedule.run_pending()
    if n == 5:
        break
