from re import findall


class NameRooShortError(Exception):
    pass


class MustContainAtStSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern_name = r"[A-Za-z]+(?=@)"
pattern_domain = r"\.[a-z]+"
valid_domains = [".com", ".bg", ".org", ".net"]
email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtStSymbolError("Email must contain @")
    elif len(findall(pattern_name, email)[0]) <= 4:
        raise NameRooShortError("Name must be more than 4 characters")
    elif findall(pattern_domain, email)[0] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    email = input()