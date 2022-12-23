import csv 

from module.Company import Company
from module.District import District

def preset_company() -> list:
    res = []
    reader = csv.reader(open("./data_set/company_presetting.csv"))
    next(reader)

    for row in reader:
        res.append(Company(float(row[1])))
    
    return res

def preset_district() -> list:
    res = []
    reader = csv.reader(open("./data_set/district_presetting.csv"))
    next(reader)

    for row in reader:
        res.append(District(int(row[1]), int(row[2]), int(row[3])))
    
    return res

global iteration_depth, map_size
iteration_depth = 6
map_size = 6
