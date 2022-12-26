# lambda
# def my(x):
#     print(3*x+2)
# result = my(5)

# def add(x, y):
#     print(x+y)
# result2 = add(90, 85)

# print((lambda x: 3*x+2)(5))
# print((lambda x,y : x+y)(90, 85))

def test(x, y):
    print(max(x,y))

max_lambda = lambda x, y : x if x > y else y

test(7,3)
print(max_lambda(7, 9))

