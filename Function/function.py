
print()
# การสร้าง function ไม่มีการ return value


def hello(name):
    print(f"Hello {name}")


# เรียกใช้งาน funtion hello ()
hello("max")

print("--------------------------")


# การสร้าง function มี return value
def area(width, height):
    total = width * height
    return total


# เรียกใช้งาน funtion area ()
print("ผลรวมพื้นที่:", area(2, 2))

print("--------------------------")


# Function ที่มีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name:{name}")
    print(f"Salary:{salary}")
    print(f"Language:{lang}")


# เรียกใช้งาน funtion show_info ()
show_info()
print()
show_info("Max", 500000, "php")
