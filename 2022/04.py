import utils

DAY = 4


class Pair:

    def __init__(self, string :str) -> "Pair":
        inf, sup = string.split("-")
        self.inf = int(inf)
        self.sup = int(sup)
    
    def contains(self, p :"Pair") -> bool:
        return self.inf <= p.inf and self.sup >= p.sup

    def overlaps_with(self, p :"Pair") -> bool:
        return (self.inf <= p.inf <= self.sup) or (self.inf <= p.sup <= self.sup)


lines = utils.read_input(DAY)

contained = 0
overlapping = 0
for line in lines:
    pair1, pair2 = map(lambda x: Pair(x), line.split(","))

    contained += (pair1.contains(pair2) or pair2.contains(pair1))
    overlapping += (pair1.overlaps_with(pair2) or pair2.overlaps_with(pair1))

utils.print_answer(1, contained)
utils.print_answer(1, overlapping)

