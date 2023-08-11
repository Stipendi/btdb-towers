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
    try:
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
    except ValueError:
        return None


def parse_towers(text):
    parts = text.split("+")
    return [x.strip() for x in parts]


def main():
    prices = read_file("tower_prices_6.18.txt")
    if prices == None:
        return 0
    while True:
        text = input("Price of: ")
        if text == "q":
            print("Exiting...")
            return 0
        total_cost = 0
        for text in parse_towers(text):
            starparts = text.split("*")
            if len(starparts) == 2:
                quantity = int(starparts[0].strip())
                text = starparts[1].lstrip()
            else:
                quantity = 1
            text = text.split(" ")
            if len(text) < 2:
                text = " ".join(text)
                print(f"Invalid tower '{text}'.")
                return 0
            upgrade = text[0]
            tower = " ".join(text[1:])
            key = find_key(tower, prices)
            if len(key) == 0:
                print(f"Could not find tower '{tower}'.")
                return 0
            elif len(key) > 1:
                print(f"Found multiple towers for '{tower}'.")
                return 0
            cost = parse_upgrade(upgrade, prices[key[0]])
            if cost == None:
                print(f"Invalid upgrade in '{upgrade}'.")
                return 0
            total_cost += cost * quantity
        print(f"It costs ${total_cost}.")


main()