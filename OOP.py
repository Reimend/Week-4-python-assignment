class person:
    def __init__(self,raymond,age,male):
         self.name = raymond
         self.age = 21
         self.gender = male
    def introduce(self):
             print(f"My name is {person.name}. I am {person.age} years old and  i am {person.gender}.")
person = person('Raymond',21,'male')
person.introduce()
             