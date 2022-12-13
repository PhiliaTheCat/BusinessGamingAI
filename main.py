from presetting import preset_company, preset_district
from copy import deepcopy

def attempt(company: list, label_c: int, district: list, label_d: int, depth: int) -> None:
    # Process
    company[label_c].add_new_branch()
    district[label_d].add_new_branch(label_c)

    # Sepcial Judge
    if depth == 4: # This line controls the depth of iteration
        cost_a: float = company[0].get_extra_cost_sum()
        cost_b: float = company[1].get_extra_cost_sum();
        sale_a: float = 0.0
        sale_b: float = 0.0
        for i in range(10): # Related to map size
            cost_a += district[i].get_basic_cost_sum(0)
            cost_b += district[i].get_basic_cost_sum(1)
            sale_a += district[i].get_virtual_sale(0)
            sale_b += district[i].get_virtual_sale(1)
        print(f"{sale_a - cost_a}, {sale_b - cost_b}")
    else:
        for i in range(10): # Related to map size
            attempt(deepcopy(company), 1 - label_c, deepcopy(district), i, depth + 1)

company = preset_company()
district = preset_district()

for i in range(10):
    attempt(deepcopy(company), 0, deepcopy(district), i, 1)
    