class District:
    def __init__(self, basic_cost: int, potential_sale: int, base_branch: int) -> None:
        self.basic_cost: int = basic_cost
        self.potential_sale: int = potential_sale
        self.base_branch: int = base_branch
        self.branch_a: int = 0
        self.branch_b: int = 0

    def get_virtual_sale(self) -> float:
        ratio: float = (self.branch_a + self.branch_b) / self.base_branch
        if ratio >= 1:
            return self.potential_sale
        else:
            return self.potential_sale * ratio