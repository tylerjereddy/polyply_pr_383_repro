"""
This is a small reproducer for the issue described at:
https://github.com/marrink-lab/polyply_1.0/pull/383#discussion_r1835118580
"""

from pathlib import Path


from polyply.src.gen_ff import gen_ff
from polyply import gen_params

def main():
    # generate the ff file
    gen_ff(itppath=Path("assets/smiles_molecule_GMX_OPLS.top"),
           smile_str="{[#Hter][#STY]|2[#ETH]|2[#BUT]|2[#STY]|2[#Hter]}.{#Hter=[>][<][H],#STY=[<]CC[>]c1ccccc1,#ETH=[<]CCCC[>],#BUT=[<]CC[>](CC)}",
           outpath="./polyply_output/OPLS_test.ff",
           res_charges=[("STY", 0), ("ETH", 0), ("BUT", 0), ("Hter", 0)])

    # generate the itp file of the same seq
    gen_params(inpath=[Path('./polyply_output/OPLS_test.ff')],
              seq=["{[#Hter][#STY]|2[#ETH]|2[#BUT]|2[#STY]|2[#Hter]}"],
              outpath=Path("./polyply_output/polymer.itp"))

if __name__ == "__main__":
    main()
