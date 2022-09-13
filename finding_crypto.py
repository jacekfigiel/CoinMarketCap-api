from json_parser import parse


def find_crypto():
    found_crypto = iterate()
    if found_crypto:
        print(found_crypto)
    else:
        print("No crypto with that name.")


def iterate():
    cryptos = parse()
    ask = input("Give a symbol of crypto:\n")
    for x in cryptos:
        if ask.upper() == x.symbol:
            return x
        elif ask.title() == x.name:
             return x
