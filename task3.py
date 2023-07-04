""" 3. Возьмите задачу о банкомате из семинара
2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""

bank = 0
count = 0
operations = []


def add_bank(cash):
    global bank, count
    bank += cash
    count += 1
    operations.append(f"Пополнение на сумму: {cash}")
    print('Ваш баланс:', bank)


def take_bank(cash):
    global bank, count
    if cash < bank:
        if (cash / 100 * 1.5) < 30:
            bank -= 30
        elif 30 < (cash / 100 * 1.5) < 600:
            bank -= cash / 100 * 1.5
        elif (cash / 100 * 1.5) > 600:
            bank -= 600
    else:
        print('Недостаточно средств!')
        return
    bank -= cash
    count += 1
    operations.append(f"Снятие на сумму: {cash}")
    print('Ваш баланс:', bank)


def exit_bank():
    print('Не забудьте забрать карту.')
    print('Список операций:')
    for operation in operations:
        print(operation)
    exit()


def check_bank():
    while True:
        cash = int(input("Введите сумму кратную 50: "))
        if cash % 50 == 0:
            return cash


def process_action(action):
    if action == '1':
        take_bank(check_bank())
    elif action == '2':
        add_bank(check_bank())
    elif action == '3':
        exit_bank()


while True:
    action = input("1 - снять\n2 - пополнить\n3 - выйти\n")
    if bank >= 5_000_000:
        bank *= 0.9
    process_action(action)

    if count == 3:
        bank *= 1.03
        count = 0

