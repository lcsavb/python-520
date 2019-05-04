# Ask the user for a string and print out whether this string is a palindrome or not.


entrada = input('Digite uma palavra'
                'para verificar se é'
                ' palíndromo: ')


def palindrome(x):
    if x[::-1] == x[:]:
        print('É palíndromo!')
    else:
        print('Não é palíndromo!')

palindrome(entrada)

entrada = input('Digite uma palavra'
                'para verificar se é'
                ' palíndromo: ')

palindrome(entrada)


