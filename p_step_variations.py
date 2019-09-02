class stair_count:
    def __init__(self, stairs, step_size):
        self.stairs = stairs
        self.step_size = step_size
        self.step_size.sort()
        self.permutations = []

    def climb(self):
        nodes_temp = []
        for i in range(len(self.step_size)):
            nodes_temp.append([self.step_size[i]])
        nodes_temp = self.node_iterate(nodes_temp)
        self.permutations.sort()

    def node_iterate(self, arrays):
        if not arrays:
            return False
        full_temp = []
        for array in arrays:
            if sum(array) > self.stairs:
                pass
            elif sum(array) == self.stairs:
                self.permutations.append(array)
            else:
                for n in range(len(self.step_size)):
                    temp = []
                    for m in array:
                        temp.append(m)
                    temp.append(self.step_size[n])
                    full_temp.append(temp)
        if len(full_temp) > 0:
            self.node_iterate(full_temp)


# create a stair_count class
sc = stair_count(4, [1, 2])
sc.climb()

# print
print(sc.permutations)
