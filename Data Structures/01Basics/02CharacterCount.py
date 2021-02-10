# Write a Program takes a string input and returns character count
def characterCount(string):
    count = dict()
    for i in string:
        if(i.isalpha()):
            if(i in count.keys()):
                count[i] += 1
            else:
                count[i] = 1
    return count


print('$'.isalpha())
string = input('Enter a string: ')
print(characterCount(string))
