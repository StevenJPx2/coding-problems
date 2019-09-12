l = [4,3,1,7,2]

# to find minimum
min_no = l[0]
for i in range(1, len(l)-1):
    if l[i] < min_no:
        min_no = l[i]
    

# removes minimum, appends last number
l.remove(min_no)
l.append(l[-1])


i = len(l)-1
while i > 0:
    l[i] = l[i-1]
    i -= 1
    
l[0] = min_no

print(l)