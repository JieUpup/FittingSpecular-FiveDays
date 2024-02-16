from refl1d.names import *
from copy import copy

fronting = SLD(name="fronting",rho=1.3196e-11)
poly = SLD(name = "poly", rho = 1.35354)
poly2 = SLD(name = " poly2", rho = 2.95368)
SiOx = SLD(name = "SoOx", rho = 3.48249)
backing = SLD (name = " backing" , rho = 2.07)

sample =(
fronting(0, 0)
    | poly(79.4147, 53.9112)
    | poly2(327.551, 24.9953)
    | SiOx(24.1576, 6.01569)
    | backing(0, 3)
)

# === Fit parameters ===
fronting.rho.range(1e-11, 1e-10)
sample[1].thickness.range(1, 200)
sample[1].interface.range(1, 100)
poly.rho.range(1, 6.5)
sample[2].thickness.range(1, 500)
sample[2].interface.range(1, 100)
poly2.rho.range(1, 6.54)
sample[3].thickness.range(10, 40)
sample[3].interface.range(5, 10)
SiOx.rho.range(3.4, 3.5)


# === Data ===
probe = load4("rawdataDay5.dat")

# === Problem definition ===
objective = Experiment(sample=sample, probe=probe)

# === Fit parameters ===
problem = FitProblem(objective)
problem.name = "day5Specular"
problem.show()
problem.save("day5_output")
problem.plot(figfile="day5_fig")


