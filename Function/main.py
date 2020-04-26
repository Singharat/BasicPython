
##########  การ Import Function จากที่อื่น ##############

# import ทั้งหมดทุก Function ใน Module
from numbers import*

# import มาบางฟังก์ชัน
from numbers import factorial, fibonacci

# import ทั้งหมดทุก Function ใน Module
import numbers

# import และเปลี่ยนชื่อฟังกฺ์ชั่น (นามแฝง) allas
from numbers import factorial as fa, fibonacci as fi

#####################################################
print()

# เรียกใช้งาน
print(numbers.factorial(5))
print(numbers.fibonacci(100))
print("--------------------------")


# เรีียกใช้งานแบบบางประกาศ import มาบางฟังก์ชัน
print(factorial(5))
print(fibonacci(100))
print("--------------------------")

# เรีียกใช้งานแบบบางประกาศ import มาแบบนามแฝง
print(fa(5))
print(fi(100))
print("--------------------------")
