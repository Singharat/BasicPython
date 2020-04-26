#Variable in Python

a = 3
b = 4.92
c = "Singharat"

print(a)
print(b)
print(c)
print(a, b, c)

# การสร้างตัวแปรหลาตัวในบรรทัดเดียว
x = y = z = 10
print(x, y, z)

j, k = 5, 15
print(j, k)

# Boolean
status = True
msg = False
print(status, msg)

# ตัวแปรแสดงรวมกับข้อความ
# วิธีที่1 concat string
print("ราคาขายต่อชิ้น", b, "บาท")

# วิธีที่2 string interpolation
print("ราคาขายต่อชิ้น %.3f บาท  " % b)
print("ราคาขายต่อชิ้น %.3f บาท มีจำนวน %d ชิ้น" % (b, a))

# วิธีที่3 format string
print(f"ราคาขายต่อชิ้น {b} บาท มีจำนวน {a} ชิ้น")
