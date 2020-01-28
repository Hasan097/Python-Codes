# 2 3 7 5 4
# 8 4 5 6 3
# 2 3 4 5 9
# 2 4 3 9 7

#a = [2, 3, 7, 5, 4]  #peak here is 7
#a = [8, 4, 5, 6, 3]  #peak here is 6
#a = [2, 3, 4, 5, 9]  #peak dne
#a = [2, 4, 3, 9, 7]  #peak here is 9
#a = [2, 3, 4, 7, 5, 3, 9] #peak dne

foot = a[0]
n = len(a)

peak = 'non-existing'
biggest = max(a)
index  = a.index(biggest)

counter = -2
breaker = 0

while breaker != 1:
    if (index + 1) == n:
        b = sorted(a)
        biggest = b[counter]
        index = a.index(biggest)

    if (index - 1) == -1:
        b = sorted(a)
        biggest = b[counter]
        index = a.index(biggest)
        
    if (index - 1) != -1 and (index + 1) != n:
        if biggest > a[index - 1] and biggest > a[index + 1]:
            peak = biggest
            breaker = 1
        else:
            counter = counter - 1

    if counter == -1*n:
        breaker = 1

print("Given List: " + str(a))
print("the peak is: " + str(peak))    


