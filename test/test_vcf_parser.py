import pytest

import vcf_to_phylip as vp

def test_vcf_parser():
    result = vp.VCF_parser("test/input.txt")
    # there should be four samples in the input file
    assert result == 4;
