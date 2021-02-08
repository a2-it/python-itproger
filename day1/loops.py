list = [6, 8, "String", 5, False, "hello"]

print('WHILE AND FOR')
print('WHile')
i = 0
while i <=10:
    print("i +=5 ", i)
    i+=5


print('list: ', list)
i=0
while i < len(list):
    print('under index:', i, '=', list[i])
    i += 1
print('\n\nFOR')
print('list: ', list)
for item in list:
    print('for item in list print: ', item)
print('\n\nBreak')
print('ролностью выходит из цикла')
print(list)
for item in list:
    if item == 5:
        break
    print(item)
print('вышла когда нашла *5*')

print('\n\nContinue\nвыходит только из нтеракции')
print(list)
for item in list:
    if item == 5:
        continue
    print(item)
print('находит *5* и дальше продолжает')