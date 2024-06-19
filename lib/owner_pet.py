class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @classmethod
    def get_all_pets(cls):
        return cls.all


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Can only add instances of Pet")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

    def get_pets(self):
        return self._pets
