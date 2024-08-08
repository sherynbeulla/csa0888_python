def remove_duplicates(arr):
     unique_elements=[]
     for num in arr:
         if not unique_element or num !=unique_elements[-1]:
             unique_elements.append(num)
             return unique_elements
            sorted_array=[1,2,3,4,6,7,6,5,3]
            result=remove_duplicates(sorted_array)
            print(result)
