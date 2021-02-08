print('Functions')
def fun():
    print('Hello World')
fun()

def func(words):
    print("Hello, ", words, "\nmasha was sent from outsiude to func()")
func("masha")

def summ(a, b, x= 0):
    res = a + b + x
    return res
print("REtURN")
print("sent 5.2.7 to summ(): ",summ(5,2,7)
      ,"\n summ() returned result, print was outside")
print(summ(5,2), 'worked only because in summ(a,b, *x = 0*)')

print('\n\n*some function may have no return, its count as err\n'
      'can be avoided if you add *pass* to that function'
      '\ndef func(words):'
      '\npass')
print('\nPARAMETERS\n')
print('the output goes as cortage(*args)')
def printAll(*args):
    print(args)
printAll(6, 8, 9, 'String')
print('\nyou can send as dictionary as well, (**args)')
def printDic(**args):
    print(args)
    print(args['long'])
    for key in args:
        print(key)
    for key, value in args.items():
        print(key, value)
printDic(long = "Georgy", short = "Gosha")
print('look at scode how to print key and values together')

print('\n\nANONYMOUS FUNCTIONS')
print('made with *lambda')

mult = lambda a, x : a*x
print(mult(2, 6))
print(mult(3, 5))

print('*args in lambda')
mult1 = lambda *args: print(args)
mult1(2, "String", False)
mult1(3, 5)
