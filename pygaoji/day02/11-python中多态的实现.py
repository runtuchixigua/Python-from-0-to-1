class Dog(object):
    def work(self):
        pass

class DrugDog(Dog):
    def work(self):
        print('追击毒品')

class GuardDog(Dog):
    def work(self):
        print('警卫')

class Person(object):
    def work_with_dog(self, dog):
        dog.work()

drug_dog = DrugDog()
guard_dog = GuardDog()
person = Person()
person.work_with_dog(drug_dog)
person.work_with_dog(guard_dog)