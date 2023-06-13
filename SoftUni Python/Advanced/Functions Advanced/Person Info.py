def get_info(name: str, town: str, age: int):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town":
    "Sofia", "age": 20}))
