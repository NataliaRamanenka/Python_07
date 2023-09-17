# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private. Соответственно,
#     для получения значений этого атрибута  нужно использовать методы get и set
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full_name(self):
        return f"{self.name} {self.surname}"

class Teather(Person):

    def __init__(self, name, surname, subject):
        super().__init__(name, surname)
        self.__subject = [subject]

    def get_subject(self):
        return (self._Teather__subject)

    def add_subject(self, new_subject):
        self._Teather__subject.append(new_subject)


t = Teather("Jone","Smith","salsa")
print(t.get_subject())
t.add_subject("tango")
print(t.get_subject())

# 5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий
