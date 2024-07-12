immutable_var = ("Ёжик", 5, 5.5)

print(immutable_var)

# immutable_var[1] = 1
# print(immutable_var)
# TypeError: 'tuple' object does not support item assignment
# Кортеж нельзя изменять, однако его вес меньше.

mutable_list = [1, "wasd", 3.4]
print(mutable_list)
mutable_list[1] = "gamer"
print(mutable_list)
