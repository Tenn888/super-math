import modules.perimeter as perimeter
import modules.factorial as factorial
import modules.tests.test_all as ta

print('pre start')
print('Start 1')
f1 = factorial.factorial_norm(5)
print(f1)   

f2 = factorial.factorial_norm(15)
print(f2)

f3 = factorial.factorial_rec(5)
print(f1)

f4 = factorial.factorial_rec(15)
print(f2)

p1 = perimeter.perimeter_func([1, 2, 5])
print(p1) 

p2 = perimeter.perimeter_func([1, 2, 5, 7, 9])
print(p2) 
print('end 2')