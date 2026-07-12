A = input("Enter the array: ")
A = list(map(int, A.split()))
largest = A[0]
sec_largest = -1
for i in range(len(A)):
    if A[i] > largest:
        sec_largest = largest
        largest = A[i]
    elif A[i] > sec_largest and A[i] != largest:
        sec_largest = A[i]
if sec_largest == -1:
    print("There is no second largest element in the array.")
else:
    print("The second largest element in the array is:", sec_largest)
    print("The largest element in the array is:", largest)