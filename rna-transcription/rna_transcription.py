def to_rna(dna_strand):
    if dna_strand == "":
        return ""
    else:
        l = []
        for c in dna_strand:
            if c == "G":
                l.append("C")
            elif c == "C":
                l.append("G")
            elif c == "T":
                l.append("A")
            elif c == "A":
                l.append("U")
            else:
                raise Exception("Not a valid DNA strand")
        return "".join(l)