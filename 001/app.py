print("Hello World")

age = 18
print(age)

name = "John"
print(name)

def say_hello():
  print("Hello World")

say_hello()

for i in range(10):
  print(i)

if True:
  print("True")
else:
  print("False")

count = 0
while (count < 10):
  print("Hello World" + str(count))
  count += 1

letters = ["a", "b", "c"]
for letter in letters:
  print(letter)

print(letters.index("b"))

map = {"a": 1, "b": 2, "c": 3}
for key, value in map.items():
  print(key, value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "red"
}

for key, value in car.items():
  print(key, value)