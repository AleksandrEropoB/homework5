immutable_var = 1, 2.2, 'red'
print(immutable_var)
# immutable_var[0]=5
# print(immutable_var)
# команда замены не выполняется, т.к. нельзя обратиться к отдельному элементу кортеж
mutable_list = ([2, 6], 'B')
print(mutable_list)

mutable_list[0][0] = "hi"
print(mutable_list)