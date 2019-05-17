"""
The Simplified Whiskas Model Python Formulation for the PuLP Modeller, converted to docplex
"""

# first import the Model class from docplex.mp
from docplex.mp.model import Model

# create one model instance, with a name
m = Model(name='The Whiskas Problem')

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

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
chickenPct = m.continuous_var(name='chickenPct')
beefPct = m.continuous_var(name='beefPct')

# Express the objective
# We want to minimize total cost of ingredients per can
m.minimize(expr=chickenPrice * chickenPct + beefPrice * beefPct)

# write constraints
# percentages sum to exactly 100
m.add_constraint(ct=chickenPct + beefPct == 100, ctname="PercentageSum")

# at least 8 grams of protein are required per can
m.add_constraint(ct=chickenProtein * chickenPct + beefProtein * beefPct >= 8.0, ctname="ProteinRequirement")

# at least 6 grams of fat are required per can
m.add_constraint(ct=chickenFat * chickenPct + beefFat * beefPct >= 6.0, ctname="FatRequirement")

# max of 2 grams of fibre allowed per can
m.add_constraint(ct=chickenFibre * chickenPct + beefFibre * beefPct <= 2.0, ctname="FibreRequirement")

# max of 0.4 grams of salt allowed per can
m.add_constraint(ct=chickenSalt * chickenPct + beefSalt * beefPct <= 0.4, ctname="SaltRequirement")

# The problem data is written to an .lp file
# prob.writeLP("WhiskasPartial.lp")
m.export_as_lp('WhiskasPartial.lp')

# The problem is solved using PuLP's choice of Solver
s = m.solve()

# print solution
m.print_solution()

# # The status of the solution is printed to the screen
# print("Status:", LpStatus[prob.status])
#
# # Each of the variables is printed with it's resolved optimum value
# for v in prob.variables():
#     print(v.name, "=", v.varValue)
#
# # The optimised objective function value is printed to the screen
# print("Total Cost of Ingredients per can = ", value(prob.objective))
