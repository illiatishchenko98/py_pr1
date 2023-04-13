# h = 'hello'
# w = 'world'

# # com = hello + ' ' + world
# # com = f"{hello} {world}"
# com = f"{str.title(h)} {str.title(w)}"

# print(com)

# def mult(a, b):
#     return a * b

# def mult(a, b): return a * b

# print(mult(5, 10))

# def greeting(greet):
#     return lambda name: f"{greet}, {name}!"

# morning_greeting = greeting('Good morning')

# print(morning_greeting('Illia'))

# evening_greeting = greeting('Good evening')

# print(evening_greeting("Illia"))

# try:
#     print('10' / 5)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("ok")

# print("Illia")


# def image_info(img):
#     if ('image_id' not in img) or ('image_title' not in img):
#         raise TypeError('Error')
#     return f"Image {img['image_title']} has {img['image_id']}"


# print(image_info({'image_title': 'My cat', 'image_id': 125}))

# try:
#     print(image_info({'image_id': 125}))
# except TypeError as e:
#     print(e)


my_list = [1, 2, 3]

first, second, third = my_list

print(first)
print(second)
print(third)


my_list = [1, 2, 3]

first, *other = my_list
print(first)
print(other)


abc = ['Illia', "see you here"]


def a(name, arg):
    return f"{name} happy to {arg}"


print(a(*abc))
