def sum_of_even_and_odd_numbers(n):
 if n <= 0:
   return "N should be a positive integer."

 even_sum = 0
 odd_sum = 0

 for i in range(1, n + 1):
   if i % 2 == 0:
     even_sum += i
   else:
     odd_sum += i

 return even_sum, odd_sum
n = int(input("Enter a positive integer: "))
even_sum, odd_sum = sum_of_even_and_odd_numbers(n)
print("Sum of even numbers from 1 to", n, ":", even_sum)
print("Sum of odd numbers from 1 to", n, ":", odd_sum)
