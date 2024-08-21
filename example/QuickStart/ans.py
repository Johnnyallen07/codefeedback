solution = {

    'e1': ([], """
def hi():
    def hello():
        print(2)
    hello()
hi()
""", {}),
    'e2': ([], """
def hi():
    def hello():
        print(2)
    hello()
hi()
""", {'structure_check': True}),
    'e3': (['a'], """
a = 2
b = 3
""", {}),
'e4': ([], """
for i in range(4):
    print(i)
""", {'check_for': True, 'ai_in_use': False}),
'e5': (['f','hi'], """
def hi():
    return "hillo"[0:2]

def f(x, y):
    return x * x + y ** 3

""", {'structure_check': False}),
'e6': (['f', 'hi'], """
def hi():
    print("hillo"[0:2])

def f(x, y):
    print(x * x + y ** 3)
""", {})
}