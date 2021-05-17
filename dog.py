class Dog:
    name="poppi"
    def __init__(self,come,eat):
        self.come=come
        self.eat=eat
    def my_dog(self):
        return f"my dog will eat {self.eat}"
    def our_dog(self):
        return f"Our dog will come {self.come}"
