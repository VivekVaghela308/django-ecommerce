class Demo():
    def first(self):
        self.a = 1
        print("hello..")
        
    def second(self):
        print(self.a)
        print("world..")
        
obj = Demo()
obj.first()
obj.second()