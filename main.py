
subor = input('Aky subor chces otvorit? ')
try:
    with open(subor, 'r') as citam:
        while True:
            content = citam.readlines()
            if not content:
                break
            print(content)
except FileNotFoundError:
    print('File not found')

zapis_text = input('Aky text chces zapisat? ')
try:
    with open('text1.txt', 'a') as zapis:
        zapis.write(zapis_text + '\n')
except Exception as e:
    print('An error occurred:', e)

print('Uprava / teray tu mam novu branch')
print('toto je nova brunch')









