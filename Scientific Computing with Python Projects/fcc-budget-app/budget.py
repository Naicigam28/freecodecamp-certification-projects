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
  category_names = [] 
  spent = []
  spent_percentages = []

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount'] 
    spent.append(round(total, 2))
    category_names.append(category.name) 

  for category_amount in spent:
    spent_percentages.append(round(category_amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"

  labels = range(100, -1 , -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "

  longest_name_length = 0
  
  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length - 1:
      graph += "\n     "

  return graph
