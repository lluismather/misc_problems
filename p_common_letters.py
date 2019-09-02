
# trials = [['ABAZDC', 'BACBAD'], ['aaaa', 'aa'], ['stringOneIsTHE BEST', 'NoStringTwoisTheBst']]
# correct = ['ABAD', 'GTAB', 'aa']

s1 = input('string one: ')
s2 = input('string two: ')
tl = input('toLower=')


class string_check:

    def __init__(self, s1, s2, toLower=False):
        self.s1 = s1
        self.s2 = s2
        if toLower:
            self.s1 = self.s1.lower()
            self.s2 = self.s2.lower()
        self.s1_list = list(self.s1)
        self.s2_list = list(self.s2)
        self.min_vecs = [0, 0]
        self.common_chars = []

    def mainloop(self):
        s1_in_s2 = [char in self.s2_list for char in self.s1_list]
        for i in range(self.min_vecs[0], len(s1_in_s2)):
            if s1_in_s2[i]:
                self.min_vecs[0] = i + 1
                for j in range(self.min_vecs[1], len(self.s2_list)):
                    if self.s1_list[i] == self.s2_list[j]:
                        self.min_vecs[1] = j + 1
                        self.common_chars.append(self.s1_list[i])
                        return True
            else:
                pass
        return False

    def find_common_chars(self):
        while self.mainloop():
            pass
        else:
            return ''.join(self.common_chars)


# takes two strings in a list, toLower argument if case.ignore
a = string_check(s1, s2, toLower=tl)
a_fin = a.find_common_chars()
print(a_fin)
