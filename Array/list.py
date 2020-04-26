
# การสร้างข้อมูลแบบ List
number = [5, 8, 13, 24, 7, 16]
name = ['John', 'Jane', 'Jany', 'Wasan']
mixed = [10, 25.75, True, 'max']

print("------------------------")

# การเข้าถึงสมาชิกใน List
print(number[1])
print(name[2])
print(mixed[2], mixed[3])
print(number)

print("------------------------")

# การนับจำนวนสมาชิกใน List
print("สมาชิกทั้งหมดของ number=", len(number))

print("------------------------")

# การสร้าง List แบบว่าง(empty list)
data = []

# การเพิ่มสมาชิกเข้าไปใน List ว่าง
data.append(10)
data.append(15)
data.append(20)
print(data)

print("------------------------")

# การ update สมาขิกใน List
data[1] = 12
print(data)

print("------------------------")

# Function วนลูปอ่านสมาชิกทั้งหมด
for n in number:
    print(n)

# Loop แล้วหาผลรวม
sum = 0
for num in number:
    sum += num
print("ผลรวม :", sum)
