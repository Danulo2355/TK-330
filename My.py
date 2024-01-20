class MyClass:
    # Initialize the global variable
    global_var = 0

    def init(self, global_var):
        # Initialize the argument with the same name as the global variable
        self.global_var = global_var
        # Increment the global variable
        MyClass.global_var += 1

    def vote(self, success):
        if success:
            self.global_var += 1
            return f"Vote succeeded! Current total: {self.global_var}"
        else:
            return f"Vote failed! Current total: {self.global_var}"

Create a new object
obj1 = MyClass(10)
print(obj1.vote(True)) # Output: Vote succeeded! Current total: 11
print(obj1.vote(False)) # Output: Vote failed! Current total: 11

Create another new object
obj2 = MyClass(20)
print(obj2.vote(True)) # Output: Vote succeeded! Current total: 22
print(obj2.vote(False)) # Output: Vote failed! Current total: 22