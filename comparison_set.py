class ComparisonSet:
    '''
    Allows you to quickly compare one sequence to many others. Effectively making
    comparison run in O(m) time instead of O(n), where m is the length of the
    sequence you are comparing with the set and n is the number of sequences you
    compare it with.
    '''

    def __init__(self):
        self.__children = {}
        self.__added = False

    def add(self, sequence):
        element = sequence[0]
        if(element not in self.__children):
            self.__children[element] = ComparisonSet()
        if(len(sequence) > 1):
            self.__children[element].add(sequence[1:])
        else:
            self.__children[element].__added = True

    def contains(self, sequence):
        if(len(sequence) == 0):
            return self.__added
        elif(sequence[0] in self.__children):
            return self.__children[sequence[0]].contains(sequence[1:])

    def common_prefix(self, sequence):
        if(len(sequence) == 0):
            return ''
        elif(sequence[0] in self.__children):
            return sequence[0] + self.__children[sequence[0]].common_prefix(sequence[1:])
        else:
            return ''

    def is_leaf(self):
        return len(self.__children) == 0

    def __to_string(self, level):
        result = ''
        for child in self.__children:
            result += '  ' * level + child + '\n'
            result += self.__children[child].__to_string(level + 1)
        return result

    def __str__(self):
        return self.__to_string(0)
