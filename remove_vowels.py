def disemvowel(word):
    new_list = list(word)
    count = 0
    for letter in new_list:
        if letter == 'a' or 'e' or 'o' or 'i' or 'u':
            #del new_list[count]
            print('letter')
            count += 1
            
    word = new_list
    print(word)
    return word

print('')
print('++++++++++++++++++++')
print('')

word = input("Enter a word: ").lower()

print('')
print('++++++++++++++++++++')
print('')

disemvowel(word)
