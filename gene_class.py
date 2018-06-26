#!/usr/bin/env python

class Gene:
    def __init__(self, creationid, creationseq):
        print("I'm a new Gene object!")
        print("My constructor got a param: " + str(creationid))
        print("Assing that param to my id instance variable...")
        self.id = creationid
        print("Similarly, assigning to my sequence instance variable...")
        self.sequence = creationseq

    def print_id(self):
        print("My id is: " + str(self.id))

    def print_sequence(self):
        print("My sequence is: " + str(self.sequence))

    def base_composition(self, base):
        base_count = 0
        for index in range(0, len(self.sequence)):
            base_i = self.sequence[index]
            if base_i == base:
                base_count = base_count + 1
        return base_count

    def gc_content(self):
        g_count = self.base_composition("G")
        c_count = self.base_composition("C")
        return (g_count + c_count)/float(len(self.sequence))

    def get_seq(self):
        return self.sequence

    def set_seq(self, newseq):
        assert self.base_composition("U") == 0, "Sorry, no RNA allowed."
        self.sequence = newseq


print("***   Creating geneA:")
geneA = Gene("AY342", "CATTGAC")

print("***   Creating geneB:")
geneB = Gene("G54B", "TTACTAGA")

print("***   Asking geneA to print_id():")
geneA.print_id()

print("***   Asking geneB to print_id():")
geneB.print_id()

print("***   Asking geneA to print_sequence():")
geneA.print_sequence()


print("***   Asking geneA to return its T content:")
geneA_t = geneA.base_composition("T")
print(geneA_t)

print("***   Asking geneA to return its GC content:")
geneA_gc = geneA.gc_content()
print(geneA_gc)


