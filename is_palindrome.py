import math


def check_for_palindrome_using_loop(word: str) -> bool:
    try:
        length = len(word)

        match length:
            case 0 | 1:
                return True
            case _:
                for id in range(math.floor(length / 2)):
                    if word[id] != word[length - (id + 1)]:
                        return False

        return True

    except Exception as e:
        print(e)


def check_for_palindrome_using_recursion(word: str) -> bool:
    try:
        length = len(word)

        match length:
            case 0 | 1:
                return True
            case _:
                if word[0] == word[length - 1]:
                    return check_for_palindrome_using_recursion(word[1 : length - 1])

        return False

    except Exception as e:
        print(e)


print("True" if check_for_palindrome_using_loop("racecar") else "False")
print("True" if check_for_palindrome_using_recursion("racecar") else "False")
