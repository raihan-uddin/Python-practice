s = "hello world"

print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.count('o'))
print(s.find('o'))

print(s.center(25, 'z'))

print('hello\thi')
print('hello\thi'.expandtabs())

s = "Hello"
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.isupper())

print("HELLO".isupper())

print(s.endswith('o'))
print(s[-1] == 'o')

print(s.split('e'))
s = 'hihihihihihi'
print(s.split('i'))
print(s.partition('i'))