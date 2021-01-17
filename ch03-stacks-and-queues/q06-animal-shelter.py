"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. People must adopt either the"oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in Linked list data structure.
"""

from collections import deque

class AnimalShelter:
    def __init__(self):
        self.cats = deque()
        self.dogs = deque()
        self.counter = 0

    def enqueue(self, genus, value):
        if genus == 'Dog':
            self.dogs.append((value, self.counter))
        elif genus == 'Cat':
            self.cats.append((value, self.counter))

        self.counter += 1

    def dequeue_any(self):
        if self.dogs and self.cats:
            dog = self.dogs.popleft()
            cat = self.cats.popleft()
            if dog[1] < cat[1]:
                self.cats.appendleft(cat)
                return dog[0]
            else:
                self.dogs.appendleft(dog)
                return cat[0]
        elif self.dogs:
            return self.dequeue_dog()
        elif self.cats:
            return self.dequeue_cat()
        else:
            raise Exception("Empty queue")

    def dequeue_dog(self):
        if not self.dogs:
            raise Exception("Empty queue")
        return self.dogs.popleft()[0]

    def dequeue_cat(self):
        if not self.cats:
            raise Exception("Empty queue")
        return self.cats.popleft()[0]

if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('Dog', 'Fido')
    shelter.enqueue('Cat', 'Garfield')
    shelter.enqueue('Dog', 'Bhoorelal')
    shelter.enqueue('Cat', 'Kaalu')
    print(shelter.dequeue_any())
    print(shelter.dequeue_dog())
    print(shelter.dequeue_cat())
    print(shelter.dequeue_cat())

