def get_good_price(price):
    price = str(price)
    price = price[::-1]
    new_price = ''
    count = 0
    for char in price:
        count += 1
        new_price += char
        if count % 3 == 0:
            new_price += " "

    new_price = new_price[::-1]
    return new_price