from pulp import LpMaximize, LpProblem, LpVariable,LpStatus,value

# Step 1: Create the problem
model = LpProblem(name="product-mix", sense=LpMaximize)

# Step 2: Define decision variables
x = LpVariable(name="Product_A", lowBound=0, cat='Continuous')
y = LpVariable(name="Product_B", lowBound=0, cat='Continuous')

# Step 3: Add constraints
model += (2 * x + y <= 100, "Machine_Time")
model += (x + y <= 80, "Labor_Hours")

# Step 4: Define objective function (maximize profit)
model += 40 * x + 30 * y, "Total_Profit"

# Step 5: Solve the problem
model.solve()

# Step 6: Print the result
print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Optimal value of Product A: {x.value()}")
print(f"Optimal value of Product B: {y.value()}")
print(f"Maximum Profit: ₹{value(model.objective)}")