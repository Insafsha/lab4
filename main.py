maxvol = 2*4  
items = {
    'rifle': {'value': 25, 'volume': 3},
    'pistol': {'value': 15, 'volume': 2},
    'ammo': {'value': 15, 'volume': 2},
    'medkit': {'value': 20, 'volume': 2},
    'inhaler': {'value': 5, 'volume': 1},  
    'knife': {'value': 15, 'volume': 1},
    'axe': {'value': 20, 'volume': 3},
    'talisman': {'value': 25, 'volume': 1},
    'flask': {'value': 15, 'volume': 1},
    'antidot': {'value': 10, 'volume': 1},  
    'supplies': {'value': 20, 'volume': 2},
    'crossbow': {'value': 20, 'volume': 2},
}

firstpoints = 20
def knap(items, maxvol=maxvol):
    nameitems = list(items.keys())
    n = len(items)
    table = [[0 for _ in range(maxvol + 1)] for _ in range(n)]
    for i, name in enumerate(nameitems):
        value = items[name]['value']
        volume = items[name]['volume']

        for curvolum in range(1, maxvol + 1):
            if i == 0:
                table[i][curvolum] = 0 if volume > curvolum else value
            else:
                without_item = table[i - 1][curvolum]
                with_item = 0
                if curvolum >= volume:
                    with_item = table[i - 1][curvolum - volume] + value
                table[i][curvolum] = max(without_item, with_item)
    sel_items = []
    remvol = maxvol
    for i in range(n - 1, -1, -1):
        if i == 0 and table[i][remvol] > 0:
            sel_items.append(nameitems[i])
        elif table[i][remvol] != table[i - 1][remvol]:
            sel_items.append(nameitems[i])
            remvol -= items[nameitems[i]]['volume']
    if "inhaler" not in sel_items:
        sel_items.append("inhaler")
        remvol -= items["inhaler"]["volume"]

    
    finalpoints = firstpoints
    for name in nameitems:
        if name in sel_items:
            finalpoints += items[name]['value']
        else:
            finalpoints -= items[name]['value']  
    if finalpoints <= 0:
        return "итоговые очки выживания отрицательные!"

    
    invent = ["."] * maxvol
    used_cells = 0
    for item in sel_items:
        for _ in range(items[item]['volume']):
            if used_cells < maxvol:
                invent[used_cells] = item[0]  
                used_cells += 1

    invent_2_4 = [invent[i:i + 4] for i in range(0, maxvol, 4)]

    # Вывод результата
    print("\nРезультат:")
    for row in invent_2_4:
        print(" ".join(row))
    print(f"Итоговые очки выживания: {finalpoints}")

if __name__ == '__main__':
    knap(items)
