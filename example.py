
# person = {
#     "name": "Tatiana",
#     "address": 3000,
#     "occupation" :"social worker"
# }

# person["name"] = "Alex"
# print(person.values())

names = ["Tats", "Felix", "Pats", "James"]
# print(names[1])
for name in names:
    print(name)

result = 0
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    result += number
    print(f"Result = {result}")

number = 0
while number < 10:
    if number == 5:
        break
    number +=1
    print(number)

def greet(name, age):
    print(f"How are you {name} your age {age}")
greet("Felix", 28)
   

character_name = "Collins"
character_age = 35
print(f"There was a man named {character_name} who was {character_age} years old")

phrase = "Moringa"
# print(f"{phrase.upper()} is cool")
print(len(phrase))