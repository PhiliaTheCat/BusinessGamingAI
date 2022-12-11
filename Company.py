class Company:
    def __init__(self, cost_modifier: float) -> None:
        self.branch: int = 0
        self.cost_modifier: float = cost_modifier
    
    def get_extra_cost(self) -> float:
        res: float = self.branch * self.cost_modifier
        return res
    
    def add_new_branch(self) -> None:
        self.branch += 1
