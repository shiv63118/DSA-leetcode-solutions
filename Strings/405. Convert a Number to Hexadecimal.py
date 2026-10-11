
def toHex(num):
    if num == 0:
        return "0"

    hexdigits = "0123456789abcdef"
    result = ""

    num &= 0xFFFFFFFF

    while num:
        result = hexdigits[num & 0xF] + result
        num >>= 4

    return result

print(toHex(-1))
