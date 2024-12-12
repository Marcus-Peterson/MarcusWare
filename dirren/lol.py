class FindPattern:
    def __init__(self, pattern):
        self.pattern =  pattern

    def findpattern(self):
        match self.pattern:
            case dict():
                return "dict()"
            case list():
                return "list()"
            case str():
                return "str()"
            case tuple():
                return "tuple()"
            

array1 = [1,2,3]
array2 = (1,2,3)
array3 = {1:1}

pattern = FindPattern(array3)

print(pattern.findpattern())