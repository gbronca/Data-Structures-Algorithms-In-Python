# Using Python way to reverse a string
reversed_string = "Hello World"[::-1]


def reverse_string(string: str) -> str:
    reversed_string = ""
    for char in string[-1::-1]:
        reversed_string += char
    return reversed_string


def reverse_string2(string: str) -> str:
    return "".join(string[-1::-1])


print(reverse_string("Hello World"))
print(reverse_string2("Hello World"))
