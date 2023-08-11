def read_file(file_name):
    prices = {}
    try:
        with open(file_name) as f:
            for row in f.readlines():
                row = row.rstrip()
                parts = row.split(":")
                if len(parts) != 2:
                    print("Invalid row (colon): \n" + row)
                    return None
                costs = [int(cost) for cost in parts[1].lstrip().split(" ")]
                if len(costs) != 9:
                    print("Invalid row (prices): \n" + row)
                    return None
                prices[parts[0]] = costs
        return prices
    except OSError:
        print("Could not read file!")


def find_key(query, dict):
    results = []
    query = query.lower()
    for key in dict.keys():
        key = key.lower()
        if query in key:
            results.append(key)
    return results


def parse_upgrade(upgrade, prices):
    parts = upgrade.split("/")
    if len(parts) != 2:
        return None
    left, right = [int(x) for x in parts]
    total = 0
    for i in range(0, left + 1):
        total += prices[i]
    if right > 0:
        for i in range(5, right + 5):
            total += prices[i]
    return total


def main():
    prices = read_file("tower_prices_6.18.txt")
    if prices == None:
        return 0
    while True:
        text = input("Price of: ")
        starparts = text.split("*")
        if len(starparts) == 2:
            quantity = int(starparts[0].strip())
            text = starparts[1].lstrip()
        else:
            quantity = 1
        text = text.split(" ")
        if text[0] == "q":
            break
        upgrade = text[0]
        tower = " ".join(text[1:])
        key = find_key(tower, prices)
        if len(key) == 0:
            print("Could not find tower!")
            continue
        elif len(key) > 1:
            print("Found multiple towers...")
            continue
        cost = parse_upgrade(upgrade, prices[key[0]])
        if cost == None:
            print("Invalid upgrade...")
            continue
        print(f"It costs ${cost * quantity}.")


main()