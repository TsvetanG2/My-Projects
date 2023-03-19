def company_users(seq):

    database = {}

    while seq != "End":
        seq = seq.split(" -> ")
        name = seq[0]
        id = seq[1]

        if name not in database:
            database[name] = list()

        if id not in database[name]:
            database[name].append(id)

        seq = input()

    for k, v in database.items():
        print(k)
        values = '\n-- '.join(v)
        print(f"-- {values}")


sequence = input()
company_users(sequence)