def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(
        kwargs.items(),
        key=lambda kvp: (-len(kvp[1]), kvp[0])
    )
    for cheeze_name, quantity in sorted_cheeses:
        result += cheeze_name + "\n"
        reversed_quantities = sorted(quantity, reverse=True)
        result += "\n".join(str(el) for el in reversed_quantities) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)