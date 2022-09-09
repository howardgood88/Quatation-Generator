import unicodedata

def wideNumInStr(s):
    def get_char_display_width(unicode_str):
        r = unicodedata.east_asian_width(unicode_str)
        if r == "W" or r == "F":  # Wide
            return 1
        else:
            return 0

    s = unicodedata.normalize('NFC', s)
    w = 0
    for c in s:
        w += get_char_display_width(c)
    # print(s, w)
    return w

def print_spliter(middle_msg, left_right_padding):
    print('-' * left_right_padding + middle_msg + '-' * left_right_padding)