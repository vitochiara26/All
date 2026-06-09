def space_jam(string):
    string = string.strip()
    message = ''
    for char in string:
        if char != ' ':
            message += char.upper()
            message += '  '
    message = message.strip()
    return message

print(space_jam("freeCodeCamp"))
print(space_jam("   free   Code   Camp   "))
print(space_jam("Hello World?!"))
print(space_jam("C@t$ & D0g$"))
print(space_jam("allyourbase"))