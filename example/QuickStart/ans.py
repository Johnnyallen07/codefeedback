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
""", {'check_for': True})
}