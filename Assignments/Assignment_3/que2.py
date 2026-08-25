#2.Write a program to input any alphabet and check whether it is vowel 
# or consonant.

ch = input('Enter an alphabet:')
if ch in ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']:
    print(f'{ch} is a vowel.')
else:
    print(f'{ch} is a consonant.')