import copy


class Collection:
    def __init__(self, array):
        """
        Constructor
        :param array: array with dominoes
        """
        self.array = array

    def get_collection(self):
        """Returns array"""
        return self.array

    def add(self, item, option):
        """Implementation in inheritance classes"""
        raise NotImplementedError("This method is not implemented in Collection type")

    def __getitem__(self, i):
        """Gives the item in the i place in the collection """
        array = self.get_collection()
        if i >= len(array) or i < 0:
            return None
        return array[i]

    def __eq__(self, other):
        """Checks if collections are equal, each domino should be equal in the value and location in the collection
        :return: True if all dominoes are equal and in place, False otherwise
        """
        if isinstance(other, Collection):
            #Checks length first, if not equal then can't be equal Collections
            if len(self.array) == len(other.array):
                for obj_num in range(len(self.array)):
                    # Checks each domino and it's place
                    if self[obj_num] == other[obj_num]:
                        continue
                    else:
                        return False
                return True
            return False
        return False

    def __ne__(self, other):
        """Checks if an array is not equal"""
        if self.array == other.array:
            return False
        return True

    def __len__(self):
        """Length of the collection"""
        return len(self.array)

    def __contains__(self, item):
        """Checks if an item is in the collection,
        :return: True if he is, False otherwise
        """
        for obj in self.array:
            if item == obj:
                return True
        return False

    def __str__(self):
        """String of the collection as requested"""
        return_str = ''
        for obj in self.array:
            return_str += str(obj)
        return return_str

    def __repr__(self):
        """Representation of collection when printed"""
        return str(self)
