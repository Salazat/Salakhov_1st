immutable_var = 7, 4, 5, float, 'code'
print(immutable_var)
#immutable_var[0] = 5
#print(tuple(immutable_var)) #Tuple относится к неизменяемым типам данных, но внутренние типы данных могут содержать изменяемый тип данных
immutable_var_1 = ([8, 5,], 0)
print(immutable_var_1)
immutable_var_1[0][1] = 8
print(immutable_var_1)
immutable_var_2=([7, 5, 9, 10], 0) + (74, 88)
print(immutable_var_2)
immutable_var_2[0][2] = 'start'
print(immutable_var_2)