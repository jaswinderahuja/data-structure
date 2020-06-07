# Author Jaswinder Singh

import pdb

class BasicOperations:

    def __init__(self):
        return None

    def gcd(self, n1, n2):
        if(n2 == 0):
            return n1
        else:
            return self.gcd(n2, n1 % n2)


class ArrayOperations(BasicOperations):

    def __init__(self):
        return None

    # array rotation juggling algorithm
    def rotate(self, array, d):
        n = len(array)
        # when d > n
        d = d % n 
        l = self.gcd(d, n)
        for i in range(l):
            temp = array[i]
            j = i
            while(1):
                k = j + d

                if(k>=n):
                    k = k - n

                if(k == i):
                    break

                array[j] = array[k]
                j = k 

            array[j] = temp

        return array



    def binary_search(self, array, item, start, end):
        if start > end:
            return -1;

        mid = int((start + end) / 2)

        if item == array[mid]:
            return mid

        if item > array[mid]:
            return self.binary_search(array, item, mid + 1, end)
        else:
            return self.binary_search(array, item, start, mid - 1)


    # Search an element in a sorted and rotated array
    def search_in_rotated_array(self, array, key, start, end):

        # pdb.set_trace()
        if start > end:
            return -1

        if array[start] < array[end]:
            return self.binary_search(array, key, start, end)
        
        mid = int((start + end) / 2)
        if array[mid] == key:
            return mid

        if array[start] < array[mid] and array[start] <= key and key <= array[mid]:
            return self.binary_search(array, key, start, mid-1)
        elif array[mid+1] < array[end] and array[mid] <= key and key <= array[end]:
            return self.binary_search(array, key, mid+1, end)
        elif key >= array[start] and key > array[mid] and array[start] > array[mid]:
            return self.search_in_rotated_array(array, key, start, mid - 1)

        else:
            return self.search_in_rotated_array(array, key, mid + 1, end)

        


    def largest_element_in_sorted_rotated(self, array):
        N = len(array)
        for index in range(N):
            if array[index] > array[(index + 1) % N]:
                end = index
                break
        start = (end + 1) % N

        return end
    # Given a sorted and rotated array, find if there is a pair with a given sum
    def pair_in_sorted_rotated(self, array, sum):
        N = len(array)
        end = self.largest_element_in_sorted_rotated(array)
        start = (end + 1) % N        
        


array_klass_obj = ArrayOperations()
print("enter array")
array = [int(i) for i in input().split(" ")]
print(array)
print("enter rotate by x")
d = int(input())
rotated_array = array_klass_obj.rotate(array, d)
print("rotated array is")
print(rotated_array)
# print(array_klass_obj.binary_search([1,2,3,4,5,6,7,55,90, 102], 55, 0,10))
while(1):
    print("enter search item, enter 0 to halt.")
    item = int(input())
    if item == 0:
        break
    print(array_klass_obj.search_in_rotated_array(rotated_array, item, 0, len(rotated_array)-1))
