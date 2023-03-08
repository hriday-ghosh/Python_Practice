'''
1. Append
Using append: we can add another 1 charachter in this List, Here, ans will be ['1', '2', '3', 7]
l = ["1", "2", "3"]
l.append(7)
print(l)
'''

'''
2. Sort
Using Sort: we can use "Sort", so the whole string will be sorted here. in this List, Here, ans will be ['1', '11', '111'] and if we write l.sort(reverse = true), then the and will decreasing order and the ans will be ['111', '11', '1']

l = ["111", "11", "1"]
l.sort(reverse=True)
print(l)
'''

'''
3. Reverse
Using Reverse: we can use "Reverse", so the whole string will be reversed, and the ans will be ['999', '99', '9'].
B = ["9", "99", "999"]
B.reverse()
print(B)
'''


'''
4. Index
Index will give the index number, so answer will be here 1 and the it works always in a first occurances.
C = ["555", "55", "5"]
print(C.index("55"))
'''


'''
5. Count
Count method will give how frequent the characher presents in the list, so answer will be here 2 as "5" comes 2 times here.
D = ["555", "55", "5", "5"]
print(D.count("5"))
'''


'''
6. Copy
Copy method will give a copy without making any changes the list.
E = ["555", "55", "5", "5"]
F = E.copy()
F[0] = 0
print(E)
'''


'''
7. Insert:
Insert method will insert the charachter at mentioned index.
Here, is our first indexes G and 1 indexes is "55"
G = ["555", "55", "5", "5"]
Then, we put G.insert(1, "999"), 1 means index no here and "999" is provided charachter here.
The answer is ['555', '999', '55', '5', '5']
G = ["555", "55", "5", "5"]
G.insert(1, "999")
print(G)

'''


'''
 8. Extend
# Extend methods simply opens another list and add another list at the end.
# So, here, H = ["1", "2", "3"] and L = ["A", "B", "C", "D"], So, here ans is ['1', '2', '3', 'A', 'B', 'C', 'D']

H = ["1", "2", "3"]
L = ["A", "B", "C", "D"]

H.extend(L)
print(H)
'''

