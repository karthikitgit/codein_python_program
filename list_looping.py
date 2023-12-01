#lst = ["45", "69", "12", "1", "55"]
    #using for loop




lst = ["45", "69", "12", "1", "55"]

for A in range (len(lst)):
    lst[A]=int(lst[A])




for A in range (len(lst)):
    for B in range (A + 1, len(lst)):
        if lst[A] < lst[B]:
            lst[A], lst[B] = lst[B] , lst[A]



lst = ["45", "69", "12", "1", "55"]
#high (69) last
#low (1) first
I = lst . index("1")
J = lst . index("45")
lst.insert(0,lst.pop(I))
lst.insert(len(lst) , lst.pop(J))
print(lst.)

#calculating of average lst
num = 0
for A in lst:
    num += int(A)
average = num  / len(lst)
print(average) #36.4

#suming all lst

num = 0
for A in (lst):
    num += int(A)
print(num) #182
#reversed the lst

reversed_lst = []
for B in lst[::-1]:
    reversed_lst.append(B)
print(reversed_lst)#['1', '55', '12', '69', '45']
