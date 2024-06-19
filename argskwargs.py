# def sum_items(*args, **kwargs):
#     print(kwargs)
#     print(args)
# sum_items(1, 3, 4, 5, k=2, a=2)
# sum_items(1, 2, 4, 5)

# def sum_items(a, b, c):
#     return a + b + c
#splat operator takes a data structure and splits into individual elements
# args = [4, 5, 5]
# args = "457"
# kwargs = {'a': 5, 'b': 6, 'c': 5}
# # x = sum_items(*args)
# x = sum_items(**kwargs)
# print(x)

# def sum_items(p1, p2, a=None, b=None, c=None):
#     print(p1, p2, a, b, c)
#     return a + b + c +p1 + p2

# # args = [1, 2]
# # kwargs = {'a': 5, 'b': 6, 'c': 5}
# # x = sum_items(*args, **kwargs)
# # print(x)
# value = [1, 2, 3, 4, 5, 5, 3, 2, 1, 5]
# print(*value)

def test(p1, *args, **kwargs):
    print(p1, args, kwargs)


values = [1, 2, 3, 4, 5, 5]
kwargs = {'a': 4, 'c': 5}
test(5, *values, **kwargs)