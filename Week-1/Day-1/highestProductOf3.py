def highest_product_of_3(list_of_ints):
   if(len(list_of_ints)<3):
       raise IndexError('Getting the product of numbers require atleast 3 numbers')
   list_of_ints.sort()
   l = len(list_of_ints)
   a = list_of_ints[l-1]*list_of_ints[l-2]*list_of_ints[l-3]
   b = list_of_ints[0]*list_of_ints[1]*list_of_ints[l-1]
   if(a>b):
       return a

   return b

li=[-99,-100,1,2,3]
print(highest_product_of_3(li))