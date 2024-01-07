"""Reverse a string"""

src: str = "ABCDEF"


def using_slice(source: str) -> str:
    """Funtion using slice"""
    return source[::-1]


def using_appending(source: str) -> str:
    """Function using appending"""

    # Recursive call escape conditions
    if len(source) == 0 or len(source) == 1:
        return source

    return using_appending(source[1:]) + source[0]


def using_swapping(source: str) -> str:
    """Function using swapping"""

    length = len(source)
    match length:
        case 0 | 1:  # Recursive call escape conditions
            return source
        case 2:
            return source[-1] + source[0]
        case _:
            return source[-1] + using_swapping(source[1:-1]) + source[0]


print(f"src = {src}")
print(f"reverse src by using_slice() = {using_slice(src)}")
print(f"src = {src}\n")

print(f"src = {src}")
print(f"reverse src by using_appending() = {using_appending(src)}")
print(f"src = {src}\n")

print(f"src = {src}")
print(f"reverse src by using_swapping() = {using_swapping(src)}")
print(f"src = {src}\n")
