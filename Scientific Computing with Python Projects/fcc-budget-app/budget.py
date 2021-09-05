class Category:
    def __init__(self,name):
        self.ledger=[]
        self.name=name
    
    def deposit(self,amount,description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self,amount,description=""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total=0
        for transaction in self.ledger:
            total+=transaction.get("amount")
        return total

    def transfer(self,amount,category):
        if(self.check_funds(amount)):
            self.withdraw(amount,f"Transfer to {category.name}")
            category.deposit(amount,f"Transfer from {self.name}")
            return True
        return False
        
    def check_funds(self,amount):
        total=0
        for transaction in self.ledger:
            total+=transaction.get("amount")
        return total-amount>=0

    def __str__(self):

        title=""
        titleLen=30-len(self.name)
        transactions=""
        for i in range(titleLen):
            title=title+"*"
            if (i+1==((titleLen)/2)):
                title=title+self.name
                
        for transaction in (self.ledger):
            amount= "{:.2f}".format(transaction.get("amount"))
            transactions=transactions+'{0: <23}{1: >7}\n'.format(transaction.get("description")[0:23],amount)
        return f"{title}\n{transactions}Total: {self.get_balance()}"

def create_spend_chart(categories):
    #TODO finish graph
    total=0
    for category in categories:
        total+=category.get_balance()
    for i in range (100,0,-10):
        print(f"{i}| ")