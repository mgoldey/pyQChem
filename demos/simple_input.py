import pyQchem as qc
test=qc.rem_fragment()
test.basis("sto-3g")
xyz=qc.cartesian()
xyz.add_atom()
xyz.add_atom("H","0","0",".74")
molec=qc.mol_fragment(xyz)
job=qc.inputfile()
job.add(test)
job.add(molec)
job.write("h2.in")
