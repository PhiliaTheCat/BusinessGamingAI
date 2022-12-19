from presetting import preset_company, preset_district, iteration_depth, map_size
from copy import deepcopy

global counter
counter = 0

def BruteForce(company: list, label_c: int, district: list, label_d: int, depth: int) -> None:
    global counter

    # Process
    company[label_c].add_new_branch()
    district[label_d].add_new_branch(label_c)

    # Sepcial Judge
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
    else:
        for i in range(map_size): # Related to map size
            BruteForce(deepcopy(company), 1 - label_c, deepcopy(district), i, depth + 1)
    counter += 1

company = preset_company()
district = preset_district()

for i in range(map_size):
    BruteForce(deepcopy(company), 0, deepcopy(district), i, 1)
print(counter)