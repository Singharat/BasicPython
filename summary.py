print("--------------------")
sumdata = 0
count = 1

while True:
    data = input(f"Enter number{count}:")
    # ตรวจผู้ใช้ป้อน 'exit'
    if data == "exit":
        break
    # การหาผลรวม//int:แปลงค่า string เป็น int
    sumdata += int(data)
    count = count+1
print(f"Sum value is{sumdata}")
