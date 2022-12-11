from presetting import preset_company, preset_district

def attempt(company: list, label_c: int, district: list, label_d: int, depth: int) -> None:
    # Special
    if depth > 2: # This line controls the depth of iteration
        for i in range(2):
            cost: float = company[i].get_extra_cost_sum()
            sale: float = 0.0
            for j in range(10):
                cost += district[j].get_basic_cost_sum(i)
                sale += district[j].get_virtual_sale(i)
            print(sale - cost)
        return

    # Process
    company[label_c].add_new_branch()
    district[label_d].add_new_branch(label_c)

    # Next Level
    for i in range(10): # Related to map size
        attempt(company[: ], 1 - label_c, district[: ], i, depth + 1)

company = preset_company()
district = preset_district()

for i in range(10):
    attempt(company[: ], 0, district[: ], i, 1)
    