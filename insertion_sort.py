#MY INSERTION_SORT
data=[5,2,4,6,1,3]
for i in range(0,len(data)):
    j=i+1
    while j<len(data):
        if data[j]<data[i]:
            k=data[i] #Need a variable key to store num in index i before it is lost
            data[i]=data[j]
            data[j]=k
        j+=1
    continue
print(data)


#From the book
data=[5,2,4,6,1,3]
for j in range(1,len(data)):
    key=data[j]
    i=j-1
    while i>-1 and data[i]>key:
        data[i+1]=data[i]
        i=i-1
    data[i+1]=key
    
print(data)


#EXERCISES
#2.1-2
#Rewriting the insertion sort procedure to work with decreasing order

data=[5,2,4,6,1,3]
for i in range(0,len(data)):
    j=i+1
    while j<len(data):
        if data[j]>data[i]:
            k=data[i]
            data[i]=data[j]
            data[j]=k
        j+=1
print(data)

#2.1-3
#Linear Search

def linear_search(data,v):
    for i in range(0,len(data)):
        if v==data[i]:
            return i
        continue
    return None
    
print(linear_search([5,2,4,6,1,3],11))

#2.1-4
#Program to add two n-bit binary integers from two different n-element arrays
#and put the resulting answer into an (n+1)-element array
A=[111]
B=[11100]
answer=[]
num1=[]
num2=[]
for i in range(0,len(A)):
    for j in range(0,len(B)):
        for bits in str(A[i]):
            num1.append(int(bits))
        for bits in str(B[j]):
            num2.append(int(bits))
        for chr1 in range(-1,(-len(num1))-1,-1):
            for chr2 in range(-1,(-len(num2))-1,-1):
                chr1j=chr1+1
                chr2j=chr2+1
                while chr1j<len(num1):
                    while chr2j<len(num2):
                        if num1[chr1]+num2[chr2]<2:
                            answer.append(num1[chr1]+num2[chr2])
                        elif num1[chr1]+num2[chr2]>=2:
                            answer.append((num1[chr1]+num2[chr2])%2)
                            ((num1[chr1j]+num2[chr2j])+(int((num1[chr1]+num2[chr2])/2)))
                        chr2j+=1
                    chr1j+=1
                break
            break
        break
    continue
print(answer) #Great BUG lol



                    























































































