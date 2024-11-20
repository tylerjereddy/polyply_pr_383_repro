"""
This is a small reproducer for the issue described at:
https://github.com/marrink-lab/polyply_1.0/pull/383#discussion_r1835118580
"""


from pathlib import Path


from polyply.src.gen_ff import gen_ff


def main():
    gen_ff(itppath=Path("assets/smiles_molecule_GMX_OPLS.top"),
           smile_str="{[#styrene]|2[#ethylene]|2[#butylene]|2[#styrene]|2}.{#styrene=[<]CC[>]c1ccccc1,#ethylene=[<]CCCC[>],#butylene=[<]CC[>](CC)}",
           outpath=".")


if __name__ == "__main__":
    main()
