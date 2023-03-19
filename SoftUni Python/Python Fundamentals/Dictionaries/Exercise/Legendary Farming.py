special_material = {
    'shards': 0,
    'fragments': 0,
    'motes': 0
}
legendary_material = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'

}
junk_material = {}

crafted = False

while not crafted:
    line = input()
    materials = line.split()

    for idx in range(0, len(materials) -1, 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in special_material:
            special_material[material] += quantity
            if special_material[material] >= 250:
                special_material[material] -= 250
                crafted = True
                print(f'{legendary_material[material]} obtained!')
                break

        else:
            if material in junk_material:
                junk_material[material] += quantity
            else:
                junk_material[material] = quantity

for material, count in special_material.items():
    print(f'{material}: {count}')

for material, count in junk_material.items():
    print(f'{material}: {count}')