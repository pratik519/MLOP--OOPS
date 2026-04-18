##initiate a class 
class employee :
    ##special fun/magic methid 
    def __init__(self):
        print("Started executing attribute and data ")
        self.id=123
        self.slaray=55000
        self.designation="SDE"
        print("Attributed And DAta Has beenn initiated")

    def travel(self,destination):
        print("the travel plan has been called mannually")
        print(f"Employee is traveling to {destination}")


##create a object/instance of the class 
sam=employee()

print(sam.id)

sam.travel("Ahmedabad")

print(type(sam))
a='x'
b='y'
print(a+b)