from presetting import preset_company, preset_district, iteration_depth, map_size
from copy import deepcopy

global counter
counter = 0

class limit:
    def __init__(self, a: float, b: float):
        self.a: float = a
        self.b: float = b

def max_a(old: limit, new: limit) -> limit:
    if (old.a < new.a):
        return new 
    else:
        return old

def max_b(old: limit, new: limit) -> limit:
    if (old.b < new.b):
        return new 
    else:
        return old

def AlphaBeta(company: list, label_c: int, district: list, label_d: int, lim0: limit, lim1: limit, depth: int) -> limit:
    global counter
    # Process
    company[label_c].add_new_branch()
    district[label_d].add_new_branch(label_c)

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
        return limit(sale_a - cost_a, sale_b - cost_b)
    
    if (1 - label_c == 0): # Company A's turn to make decision
        for i in range(map_size): # Related to map size
            lim0 = max_a(lim0, AlphaBeta(deepcopy(company), 1 - label_c, deepcopy(district), i, deepcopy(lim0), deepcopy(lim1), depth + 1))
            if lim0.b < lim1.b:
                counter += 1
                return lim1
        counter += 1
        return lim0
    else: # Company B's turn to make decision
        for i in range(map_size): # Related to map size
            lim1 = max_b(lim1, AlphaBeta(deepcopy(company), 1 - label_c, deepcopy(district), i, deepcopy(lim0), deepcopy(lim1), depth + 1))
            if lim0.a > lim1.a:
                counter += 1
                return lim0
        counter += 1
        return lim1
        

company = preset_company()
district = preset_district()

lim0: limit = limit(-10000000, -10000000)
lim1: limit = limit(-10000000, -10000000)

for i in range(map_size): # Related to map size
    lim0 = max_a(lim0, AlphaBeta(deepcopy(company), 0, deepcopy(district), i, deepcopy(lim0), deepcopy(lim1), 1))
print(f"{lim0.a}, {lim0.b}")
print(counter)
