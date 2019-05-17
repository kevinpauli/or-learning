"""
The Simplified Whiskas Model Python Formulation for the PuLP Modeller

Authors: Antony Phillips, Dr Stuart Mitchell  2007
"""

# Import PuLP modeler functions
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem(name='The Whiskas Problem', sense=LpMinimize)

chickenPrice = 0.013
chickenProtein = 0.100
chickenFat = 0.080
chickenFibre = 0.001
chickenSalt = 0.002

beefPrice = 0.008
beefProtein = 0.200
beefFat = 0.100
beefFibre = 0.005
beefSalt = 0.005

# The 2 variables Beef and Chicken are created with a lower limit of zero
chickenPct = LpVariable(name="ChickenPercent", lowBound=0, upBound=None, cat=LpInteger)
beefPct = LpVariable(name="BeefPercent", lowBound=0)

# The objective function is added to 'prob' first
prob += (chickenPrice * chickenPct + beefPrice * beefPct, "Total Cost of Ingredients per can")

# The five constraints are entered
prob += (chickenPct + beefPct == 100, "PercentagesSum")
prob += (chickenProtein * chickenPct + beefProtein * beefPct >= 8.0, "ProteinRequirement")
prob += (chickenFat * chickenPct + beefFat * beefPct >= 6.0, "FatRequirement")
prob += (chickenFibre * chickenPct + beefFibre * beefPct <= 2.0, "FibreRequirement")
prob += (chickenSalt * chickenPct + beefSalt * beefPct <= 0.4, "SaltRequirement")

# The problem data is written to an .lp file
prob.writeLP("WhiskasPartial.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Ingredients per can = ", value(prob.objective))
