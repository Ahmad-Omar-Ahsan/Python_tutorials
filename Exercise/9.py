fin = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
# for line in fin:
# word = line.strip()
# #print(word)

# 9.1

"""
def read_txt(fObject):
    for line in fObject:
        word = line.strip()
        if len(word) > 20:
            print(word)

"""


# read_txt(fin)


def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

# 9.3


def read_txt(file_object):
    total_length = 0
    word_printed = 0
    for line in file_object:
        word = line.strip()
        total_length = total_length + 1
        if has_no_e(word):
            print(word)
            word_printed = word_printed + 1
    percentage = word_printed * 100/total_length
    print(round(percentage, 2), end='%')


# 9.4


def avoids(word, string):
    if string in word:
        return False
    else:
        return True


# string = input('Enter a string of forbidden numbers: ')


def read_txt(file_object):
    total_length = 0
    word_printed = 0
    for line in file_object:
        word = line.strip()
        total_length = total_length + 1
        if cartalk(word):
            print(word)
            word_printed = word_printed + 1
    print('total_length: ' + str(total_length))
    print('word_printed: ' + str(word_printed))


# read_txt(fin, string)


# 9.4

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True


# 9.5


def uses_all(word, string):
    return uses_only(string, word)


# 9.6


def is_abecedarian(word):
    if len(word) == 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


# read_txt(fin)


# 9.7


def is_triple_word(word):
    len_w = len(word)
    i = 0
    count = 0
    while i < len_w - 1:
        if word[i] == word[i + 1]:
            i = i+2
            count = count + 1
        else:
            i = i + 1
            count = 0
    if count == 3:
        return True
    else:
        return False


def find_triple_world():
    finx = open(r'C:\Users\Ahmad Omar Ahsan\Documents\words.txt')
    for line in finx:
        word = line.strip()
        if is_triple_word(word):
            print(word)


find_triple_world()


# 9.8


def has_palindrome(i, start, len):
    """
    returns true if integer i as a string has palindrome with length len and starting index start
    :param i: integer i
    :param start: starting index
    :param len: length of string
    :return: returns true if palindrome exist
    """
    s = str(i)[start:start + len]
    return s[::-1] == s


# c = 'potato'[0:0+len('potato') - 1]
# print(c)


def palindrome(i):
    """
    check if i has the property claimed by the puzzler
    :param i: integer i
    :return: returns true if it does
    """
    return has_palindrome(i, 2, 4) and has_palindrome(i + 1, 1, 5) and has_palindrome(i + 2, 1, 4) and has_palindrome(i + 3, 0, 6)


def print_all():
    for i in range(100000, 1000000):
        if palindrome(i):
            print(i)


print_all()


# 9.9


def str_fill(i, len):
    return str(i).zfill(len)


def arr_rev(i, j):
    return str_fill(i, 2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if arr_rev(daughter, mother) or arr_rev(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)