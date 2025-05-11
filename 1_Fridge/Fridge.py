from decimal import Decimal
from datetime import datetime, date

date_format = '%Y-%m-%d'

goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal('0.5'), 'expiration_date': date(2025, 4, 15)}
    ]
}


def add(items, title, amount, expiration_date=None):
    expiration_date = (None if expiration_date is None else datetime.strptime(expiration_date, date_format).date())

    if title in items:
        list.append(items[title], {'amount': amount, 'expiration_date': expiration_date})
    else:
        items[title] = [{'amount': amount, 'expiration_date': expiration_date}]


def add_by_note(items, note):
    parts = note.split(' ')

    expiration_date_list = parts[-1].split('-')
    if len(expiration_date_list) == 3:
        expiration_date = parts[-1]
        amount = parts[-2]
        title = ' '.join(parts[0:-2])
    else:
        expiration_date = None
        amount = parts[-1]
        title = str.join(' ', parts[0:-1])

    add(items, title, Decimal(amount), expiration_date)


def find(items, needle):
    result = []
    for title in items.keys():
        if str.upper(needle) in str.upper(title):
            result.append(title)
    return result


def get_amount(items, needle):
    count = Decimal('0')
    for title, params in items.items():
        if str.upper(needle) in str.upper(title):
            for param in params:
                count += param['amount']

    return count


def get_expired(items, in_advance_days=0):
    today = date.today()
    expired_goods = []

    for title, params in items.items():
        count = Decimal('0')
        for param in params:
            expiration_date = param['expiration_date']
            if expiration_date is not None and (expiration_date - today).days <= in_advance_days:
                count += param['amount']
        if count > 0:
            expired_goods.append((title, Decimal(count)))

    return expired_goods


# print(goods)

add(goods, 'Пельмени Универсальные', Decimal('1.5'), '2025-05-28')
add(goods, 'Яйца', Decimal('10'), '2025-05-12')
add(goods, 'Яйца', Decimal('20'), '2025-06-12')
add(goods, 'Каша', Decimal('1'))

add_by_note(goods, 'Яйца гусиные 4 2025-05-09')
add_by_note(goods, 'Вода 1.5')
add_by_note(goods, 'Яйца Фабрики №1 4 2025-07-15')

# print(find(goods, 'Яйц'))

# print(get_amount(goods, 'яйца'))
# print(get_amount(goods, 'морковь'))

print(get_expired(goods))
print(get_expired(goods, 30))

# print(goods)
