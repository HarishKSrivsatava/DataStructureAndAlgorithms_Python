tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );

# Access
print(tup1[:]) # ('physics', 'chemistry', 1997, 2000)
print(tup1[:-1]) #('physics', 'chemistry', 1997)

# Updation
tup3 = (12, 34.56);
tup4 = ('abc', 'xyz');
#tup4[0] = 'test' # TypeError: 'tuple' object does not support item assignment
tup5 = tup3+tup4
print(tup5) #(12, 34.56, 'abc', 'xyz')

# Deletion
tup = ('physics', 'chemistry', 1997, 2000);
print(tup)
del tup
print(tup) #NameError: name 'tup' is not defined