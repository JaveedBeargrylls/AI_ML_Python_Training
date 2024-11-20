class mylaptop:
    a=67
    data="hello"
 
obj=mylaptop()
 
print(obj.a)
print(obj.data)
 
 
print(mylaptop.a)
print(mylaptop.data)
 
#####################################
 
 
class mylaptop:
    def __init__(self,ram,processor):
        self.ram=ram
        self.processor=processor
 
    def config(self):
        print(self.ram)
        print(self.processor)
 
 
newobj=mylaptop("16 GB","i3")
newobj.config()
newobj.ram="32 GB"
newobj.config()
 
 
 
########################
 
class laptop:
    def hp_laptop(self):
        return "my HP laptop"
    def machine_learning(self):
        return "way to impliment AI"
 
class PC(laptop):
    def PC_config(self):
        return "using for graphics team"
    def AI(self):
        return "collection of algorithms"
   
notebook=laptop()
zenbook=PC()
print(notebook.machine_learning())
print(zenbook.PC_config())
print(zenbook.machine_learning())


##########################################

class mylaptop:
    def __init__(self,ram,processor):
        self.ram=ram
        self.processor=processor
        print(self.ram)
    
    def machine_learning(self):
        return "working with ML app"
    
    def config(self):
        return(self.ram)

class new(mylaptop):
    def __init__(self, ram, processor, HD):
        super().__init__(ram,processor)
        self.HD=HD
        print(self.HD)

obj1=mylaptop("32 GB","i3")
obj2=new("168 GB","i5","500 GB")

print(obj2.machine_learning())
print(obj2.config())

##############################################

class account:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.__balance=balance
 
    def get_balance(self):
        return self.__balance
   
    def update_balance(self,amount):
        if amount>0:
            self.__balance +=amount
            print(amount)
        else:
            print("Invalid amount")
   
 
acc=account("ashish",1000)
print(acc.account_holder)
print(acc.get_balance())
acc.update_balance(5000)
 
print(acc.get_balance())