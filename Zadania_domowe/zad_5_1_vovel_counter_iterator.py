'''
Zaimplementuj iterator zwracający jedynie samogłoski z zadanego ciągu znaków:
​
Przykładowe użycie:
for char in Vowels('ala ma kota a kot ma ale'):
'''


class VolelCouner:
    VOVELS = ['e', 'y', 'u', 'i', 'o', 'a']

    def __init__(self, text_to_count: str):
        """
        class for counting vovels in the string using iterator
        :type text_to_count: object
        """
        self.text_to_count = text_to_count

    def __iter__(self):

        print("Iteration started")
        self.char_counter = 0
        return self

    def __next__(self):
        print("Next")

        self.string_lenght = len(self.text_to_count)
        self.how_much_vovels = 0
        vovels = []

        if self.char_counter > self.string_lenght:
            raise StopIteration


        for char in self.text_to_count:
            self.char_counter += 1
            if char in self.__class__.VOVELS:
                self.how_much_vovels += 1
                vovels.append(char)
            else:
                self.char_counter += 1

        return f'Amount of vovels: {self.how_much_vovels}\n{vovels}'


zlicz = VolelCouner("co to ma byc do cholery")

for char in zlicz:
    print(char)

print('=' * 60)

zlicz2 = VolelCouner("lorem impum lorem ipsum lorem impus")
for char in zlicz2:
    print(char)