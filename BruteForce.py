from module.presetting import preset_company, preset_district, iteration_depth, map_size
from copy import deepcopy
from module.Limit import Limit, max_a, max_b

global counter
counter = 0

def BruteForce(company: list, label_c: int, district: list, label_d: int, lim: Limit, depth: int, path: list) -> Limit:
    global counter

    # Process
    company[label_c].add_new_branch()
    district[label_d].add_new_branch(label_c)
    path.append(label_d)

    # Special Judge
    if depth == iteration_depth: # This line controls the depth of iteration
        cost_a: float = company[0].get_extra_cost_sum()
        cost_b: float = company[1].get_extra_cost_sum();
        sale_a: float = 0.0
        sale_b: float = 0.0
        for i in range(map_size): # Related to map size
            cost_a += district[i].get_basic_cost_sum(0)
            cost_b += district[i].get_basic_cost_sum(1)
            sale_a += district[i].get_virtual_sale(0)
            sale_b += district[i].get_virtual_sale(1)
        counter += 1
        return Limit(sale_a - cost_a, sale_b - cost_b, deepcopy(path))
    
    if (1 - label_c == 0): # Company A's turn to make decision
        for i in range(map_size): # Related to map size
            lim = max_a(lim, BruteForce(deepcopy(company), 1 - label_c, deepcopy(district), i, deepcopy(lim), depth + 1, deepcopy(path)))
        return lim
    else: # Company B's turn to make decision
        for i in range(map_size): # Related to map size
            lim = max_b(lim, BruteForce(deepcopy(company), 1 - label_c, deepcopy(district), i, deepcopy(lim), depth + 1, deepcopy(path)))
        return lim
        

company = preset_company()
district = preset_district()

lim: Limit = Limit(-10000000, -10000000, [])

for i in range(map_size): # Related to map size
    lim = max_a(lim, BruteForce(deepcopy(company), 0, deepcopy(district), i, lim, 1, []))
print(f"{lim.a}")
i: int = 0
for label in lim.path:
    if (i % 2 == 0):
        print(f"{label}")
    i += 1

lim: Limit = Limit(-10000000, -10000000, [])

for i in range(map_size): # Related to map size
    lim = max_b(lim, BruteForce(deepcopy(company), 1, deepcopy(district), i, lim, 1, []))
print(f"{lim.b}")
i = 0
for label in lim.path:
    if (i % 2 == 0):
        print(f"{label}")
    i += 1

print(counter)


def BruteForce(company: list, label_c: int, district: list, label_d: int, lim: Limit, depth: int, path: list) -> Limit:
    # Apply demanded actions
    company[label_c].add_new_branch()
    district[label_d].add_new_branch(label_c)
    path.append(label_d)
