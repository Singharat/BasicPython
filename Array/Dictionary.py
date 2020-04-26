# การเก็บข้อมูลเป็นคู๋ (key:value)
scores = {'john': 1200,
          'bobby': 2000,
          'janny': 4200
          }

print(scores)
print("Bobby :", scores['bobby'])

print("---------------------")

# เพิ่มสมาชิกใหม่เข้า Dictionary
scores['roger'] = 3200
print(scores)

print("---------------------")

# การสร้าง Dictionary ว่าง
points = {}

# เพิ่มค่าเข้าไปใน Dixtionary
points['mr_a'] = 10.2
points['mr_b'] = 15.4
points['mr_c'] = 22.8

print(points)

print("---------------------")

# การ Loop อ่านสมาชิกของ Dictionary ออกมา
for k, v in scores.items():
    print(k, v)
