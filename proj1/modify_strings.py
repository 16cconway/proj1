def reverse_string(str1: str) -> str:
    """
    Reserves the input string's characters
    :param str1: input string
    :return: str2: The reverse of str1
    """
    str2 = ""
    for char in str1:
        str2 = char + str2
    return str2


def strip_string(str1: str) -> str:
    """
    Strips input string of all \n, \t, and spaces
    :param str1: input string
    :return: final_string: original string with no whitespace or new line
    characters
    """
    final_string = ""
    for char in str1:
        if char == "\n" or char == "\t" or char == " ":
            continue
        else:
            final_string = final_string + char
    return final_string
