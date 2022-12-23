class District:
    def __init__(self, basic_cost: int, potential_sale: int, base_branch: int) -> None:
        self.basic_cost: int = basic_cost
        self.potential_sale: int = potential_sale
        self.base_branch: int = base_branch
        self.branch_a: int = 0
        self.branch_b: int = 0

    def get_virtual_sale(self, label: int) -> float:
        if self.branch_a + self.branch_b == 0:
            return 0.0
        ratio: float = (self.branch_a + self.branch_b) / self.base_branch
        if ratio >= 1:
            ratio = 1.0
        if label == 0:
            res: float = ratio * self.potential_sale * self.branch_a / (self.branch_a + self.branch_b)
        else:
            res: float = ratio * self.potential_sale * self.branch_b / (self.branch_a + self.branch_b)
        return res

    def get_basic_cost_sum(self, label: int) -> int:
        if label == 0:
            res: int = self.basic_cost * self.branch_a
        else: 
            res: int = self.basic_cost * self.branch_b
        return res
    
    def add_new_branch(self, label: int) -> None:
        if label == 0:
            self.branch_a += 1
        else:
            self.branch_b += 1
