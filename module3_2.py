variants = ('.com','.ru','.net')
def send_email(message, recipient,*, sender = 'university.help@gmail.com'):
    if ("@" not in recipient or recipient.endswith(variants) != True) and ("@" not in sender or sender.endswith(variants) != True):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient, '.')
    else:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправленно с адреса ', sender, ' на адрес ', recipient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)

send_email('Это сообщение для проверки связи', 'vasuok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.students@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
