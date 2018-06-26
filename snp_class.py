#!/usr/bin/env python


class SNP:
    """SNP object from VCF file format."""
    def __init__(self, reference_allele, alternative_allele, chromosome_name, reference_position, snp_id):
        self.reference_allele = reference_allele
        self.alternative_allele = alternative_allele
        self.chromosome_name = chromosome_name
        self.reference_position = reference_position
        self.snp_id = snp_id

    def is_transition(self):
        if self.reference_allele == 'A' and self.alternative_allele == 'G':
            return True
        elif self.alternative_allele == 'A' and self.reference_allele == 'G':
            return True
        elif self.reference_allele == 'C' and self.alternative_allele == 'T':
            return True
        elif self.alternative_allele == 'C' and self.reference_allele == 'T':
            return True
        else:
            return False

    def is_transversion(self):
        if self.is_transition:
            return False
        else:
            return True


snpA = SNP("A", "G", 1, 799739, 'rs57181708')
print (snpA.is_transition())
print (snpA.is_transversion())