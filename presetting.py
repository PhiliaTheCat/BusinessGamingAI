import csv 

from Company import Company
from District import District

def preset_company() -> list:
    res = []
    reader = csv.reader(open("./company_presetting.csv"))
    next(reader)

    for row in reader:
        res.append(Company(float(row[1])))
    
    return res

def preset_district() -> list:
    res = []
    reader = csv.reader(open("./district_presetting.csv"))
    next(reader)

    for row in reader:
        res.append(District(int(row[1]), int(row[2]), int(row[3])))
    
    return res
