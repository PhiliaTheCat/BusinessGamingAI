from module.presetting import preset_company, preset_district, iteration_depth, map_size
from copy import deepcopy
from module.Limit import Limit, max_a, max_b

global counter
counter = 0

def AlphaBeta(company: list, label_c: int, district: list, label_d: int, lim0: Limit, lim1: Limit, depth: int, path: list) -> Limit:
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
            lim0 = max_a(lim0, AlphaBeta(deepcopy(company), 1 - label_c, deepcopy(district), i, deepcopy(lim0), lim1, depth + 1, deepcopy(path)))
            if lim0.b <= lim1.b:
                return lim1
        return lim0
    else: # Company B's turn to make decision
        for i in range(map_size): # Related to map size
            lim1 = max_b(lim1, AlphaBeta(deepcopy(company), 1 - label_c, deepcopy(district), i, lim0, deepcopy(lim1), depth + 1, deepcopy(path)))
            if lim1.a <= lim0.a:
                return lim0
        return lim1
        

company = preset_company()
district = preset_district()

lim0: Limit = Limit(-10000000, -10000000, [])
lim1: Limit = Limit(-10000000, -10000000, [])

for i in range(map_size): # Related to map size
    lim0 = max_a(lim0, AlphaBeta(deepcopy(company), 0, deepcopy(district), i, deepcopy(lim0), lim1, 1, []))
    if lim0.b <= lim1.b:
        lim0 = lim1
        break
print(f"{lim0.a}")
i: int = 0
for label in lim0.path:
    if (i % 2 == 0):
        print(f"{label}")
    i += 1

lim0: Limit = Limit(-10000000, -10000000, [])
lim1: Limit = Limit(-10000000, -10000000, [])

for i in range(map_size): # Related to map size
    lim1 = max_b(lim1, AlphaBeta(deepcopy(company), 1, deepcopy(district), i, lim0, deepcopy(lim1), 1, []))
    if lim1.a <= lim0.a:
        lim1 = lim0
        break
print(f"{lim1.b}")
i = 0
for label in lim1.path:
    if (i % 2 == 0):
        print(f"{label}")
    i += 1

print(counter)
