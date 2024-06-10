class Category:
    def __init__(self,category):
        self.category=category
        self.ledger=[]

    def deposit(self,amount,description=""):
        self.ledger.append({"amount":amount,"description":description})

    def withdraw(self,amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount,"description":description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance=0
        for amount in self.ledger:
            balance+=amount["amount"]
        return balance
    
    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self,amount):
         return True if self.get_balance()>=amount else False

    def __str__(self):
        str_f=""
        str_f+=self.category.center(30,"*") + "\n"
        #string formatting
        '''
        max_num=0
        max_amnt=0   
        for key in self.ledger:
            if len(key["description"][:23])>max_num:
                max_num=len(key["description"][:23])
            if len(f'{key["amount"]:.2f}')>max_amnt:
                max_amnt=len(f'{key["amount"]:.2f}')
        '''
        for item in self.ledger:
            descr=item['description'][:23]
            amt=f'{item["amount"]:.2f}'
            #length=len(item['description'][:23])
            #str_f+=(amt).rjust((max_num+max_amnt)-(length))+'\n' 
            str_f+= f"{descr.ljust(23)}{amt.rjust(7)}\n"
        str_f+=f"Total: {str(self.get_balance())}"
        return str_f

def create_spend_chart(categories):
    spending={}
    total=0
    for cet in categories:
        spending[cet.category]=0
        for amts in cet.ledger:
            spending[cet.category]+=abs(amts["amount"]) if amts["amount"]<0 else 0
    for i in spending:
        total+=spending[i]
    percent_dict = {}
    for i in spending.keys():
        percent_dict[i] = int(round(spending[i]/total,2)*100)

    fin_str=""
    fin_str+="Percentage spent by category\n"
    for j in range(100,-10,-10):
        fin_str += f'{j}'.rjust(3) + '| '
        for percent in percent_dict.values():
            fin_str+="o  " if percent>=j else "   "
        fin_str+="\n"
    fin_str+=" "*4
    fin_str+=(3*len(categories)+1)*"-"+"\n"
    cats=[cat.category for cat in categories]
    biggest=len(max(cats,key=len))
    for l in range(biggest):
        fin_str+="     "
        for m in cats:
            try:
                fin_str+=m[l]+"  "
            except:
                fin_str+="   "
        if l < biggest-1:
            fin_str+="\n"
    return fin_str

food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
auto=Category("Auto")
auto.deposit(1000, "deposit")
auto.withdraw(500)
clothing.withdraw(2.4)
print(create_spend_chart([food,clothing,auto]))
