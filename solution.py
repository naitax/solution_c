''' Testing #1
test = {
    'viewonly': [1, 2, 3, 4, 5, 6, 7],
    'admin': [4, 5, 6, 111, 23, 45]
}
s = input()
numbers = set(map(int, s.split()))
l = len(test)
x = []
new_set_roles = []
keys = []
dicts = {}
new_set_roles = list(test.keys())
new_dicts = []
for i in range(l):
    new_set = numbers.intersection(set(list(test.values())[i]))
    x.append(new_set)
    k = len(new_set)
    keys.append(k)
    dicts[keys[i]] = x[i]
    #new_dicts[new_set_roles[i]] = dicts[i]
print(new_set_roles)
#print(dicts)
# print maximum value
#maximum = max(dicts, key=dicts.get)  # Just use 'min' instead of 'max' for minimum.
#print(maximum, dicts[maximum])
print(dicts)
dicts_sorted_keys = sorted(dicts, key=dicts.get, reverse=True)
for r in dicts_sorted_keys:
    print('Number of corresponding programs: {}, list of programs: {}'.format(r, dicts[r]))
#print(test.values())
'''
#################################################################
import json

with open('data.json') as json_file:
    test = json.load(json_file)

s = input('Please enter names of programs you need to have access to: ').upper()
numbers = set(map(str, s.split()))
l = len(test)
x = []
new_set_roles = []
keys = []
dicts = {}
new_set_roles = list(test.keys())
new_dicts = []
for i in range(l):
    new_set = numbers.intersection(set(list(test.values())[i]))
    x.append(new_set)
    k = new_set_roles[i]
    keys.append(k)
    dicts[keys[i]] = x[i]


dicts_sorted_keys = sorted(dicts, key=dicts.get, reverse=True)
for r in dicts_sorted_keys:
    if len(dicts[r]) == 0:
        continue
    print('Role: {}, number of programs: {}/{}, list of corresponding programs: {}, total list of programs: {}'.format(r.upper(), len(dicts[r]), len(numbers), dicts[r], len(test[r])))

