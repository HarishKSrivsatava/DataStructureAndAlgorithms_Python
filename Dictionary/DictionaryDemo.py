dict1 = {
            1:"test",
            2:10
        }

# Access the elements
print(dict1) #{1: 'test', 2: 10}
print(dict1[2]) #10
#print(dict[3]) #TypeError: 'type' object is not subscriptable

# Length of the dictionary
print(len(dict1)) #2
#print(dict1.key())

myDict = {1:"James" , 2: "Bond"}
print(myDict.values()) #dict_values(['James', 'Bond'])
print(myDict.keys()) #dict_keys([1, 2])
print(myDict.items()) #dict_items([(1, 'James'), (2, 'Bond')])
print(myDict.get(1)) #James

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict)
del dict['Name']; # remove entry with key 'Name'
print(dict) #{'Age': 7, 'Class': 'First'}
dict.clear();     # remove all entries in dict
print(dict) #{}
del dict ;        # delete entire dictionary
print(dict) #<class 'dict'>


dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Katheren'}
print (dict['Name']) #Katheren

dict2 = {['Name']: 'Zara', 'Age': 7}
print(dict2['Name'])
print ("dict2['Name']: ", dict2['Name'])