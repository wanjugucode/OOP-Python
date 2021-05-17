class Car:
    name="Dotty"
    def __init__(self,refill,crush):
        self.refill=refill
        self.crush=crush
    def my_car(self):
        return f"I will refill {self.refill}"
    def brown_car(self):
        return f"These car crushed {self.crush}"