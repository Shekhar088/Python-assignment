def PrimeSum():
    sum=0
    #check if its a prime number
    for number in range(0,len(arr)):
        if arr[number]>1:
            for numbers in range(2, arr[number]):
                if (arr[number] % numbers) ==0:
                    break
            else:
                p.append(arr[number])

    print("The array of given numbers are:\n" f"{arr}")  
    print("The array of prime numbers from given array are:\n" f"{p}")
    #calcuate square sum
    for i in range(0,len(p)):
        sum = sum+pow(p[i],2)
    return sum

    
a = int(input("Enter a length of array"))
arr=[]
for i in range(0,a):
    print("Enter the " f"{i} element:")
    element = int(input())
    arr.append(element)

p=[]

print("The sum of the squares of prime number is:" f"{PrimeSum()}")