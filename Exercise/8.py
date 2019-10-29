# 8.1
fruit = 'banana'
index= len(fruit) - 1
while index >= 0:
    print(fruit[index], end='')
    index = index - 1

# 8.2
print()

"""
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

s = 'Monty Python'
print(s[0:5])
print(s[6:13])
"""
#8.3


def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


#print(find('Gurantee', 'e', 2))

#8.5


def count(word, letter):
    count = 0
    index = 0
    while index < len(word):
        index = find(word, letter, index)
        if index != -1:
            count = count + 1
        else:
            break
        index = index + 1
    print(count)


#count('rose', 'a')

name = 'bob'
#print(name.find('b', 1, 3))
fruit = 'banana'
#print(fruit.count('a', 1, 6))

# 8.8


def is_reverse(word1, word2):
    if len(word1) !=  len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        # print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
    return True


#print(is_reverse('pots', 'stop'))


# 8.9
def is_palindrome(word):
    if word == word[::-1]:
        print(True)
    else:
        print(False)


#is_palindrome('mom')


#8.12
def rotate_word(word, key):
    for i in range(len(word)):
        old_letter = word[i]
        print(old_letter, end=' ')
        int_char = ord(word[i])
        new_int_char = int_char + key
        new_letter = chr(new_int_char)
        print(new_letter)
        word = word.replace(old_letter, new_letter, 1)
    print(word)


rotate_word('melon', -1)
