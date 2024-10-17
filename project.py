import csv


class New_Costomer :

  all_costomer = []
  
  def __init__ (self, acc_name, age, job, id, phone, bank_acc, balance):
    self.account_name = acc_name
    self.age = age
    self.job_title = job
    self.id = id 
    self.phone = phone 
    self.bank_account = bank_acc
    self.balance = balance
    New_Costomer.all_costomer.append(self)

  def __str__ (self) :
    return f"costomer name: {self.account_name}  \nphone number: {self.phone} \njob title: {self.job_title} \nID: {self.id} \nbank account: {self.bank_account} \nage: {self.age} \nbalance: {self.balance}"

  def __repr__(self):
    return f"costomer name: {self.account_name}  \nphone number: {self.phone} \njob title: {self.job_title} \nID: {self.id} \nbank account: {self.bank_account} \nage: {self.age} \nbalance: {self.balance}"

  def view_balance (self):
    print(f"New {self.account_name}`s balance is {self.balance}")

  def add_amount (self, bank_acc, amount):
    if bank_acc == self.bank_account :
      self.balance += amount
      print (f"New {self.account_name}`s balance is {self.balance}")
    else:
      print ("Can`t Acces To This Account")
  
  def withdraw (self, bank_acc, amount):
    if bank_acc == self.bank_account :
      if self.balance >= amount:
        self.balance -= amount
        print (f"New {self.account_name}`s balance is {self.balance}")
      else:
        print("not enough money")
    else:
      print ("Can`t Acces To This Account")

  @classmethod
  # cls refer to class method 
  def costomers_list(cls , data_file):
    with open(data_file, "r") as costomers_file :
      csv_reader = csv.DictReader(costomers_file)
      for emp in csv_reader :
        name = emp["name"]
        age = emp["age"]
        job = emp["job_title"]
        id = emp["id"]
        phone = emp["phone"]
        bank_acc = emp["bank_account"]
        balance = emp["balance"]
        cls(name ,age ,job ,id ,phone ,bank_acc ,balance)


New_Costomer.costomers_list("costomers_data.csv")

#let`s do some data anlyisetics

# print all costomers
print(New_Costomer.all_costomer)
for emp in New_Costomer.all_costomer:
  print(emp)
  print("-"*30)

# print costomer by who get over 5000$
new_list = [emp for emp in New_Costomer.all_costomer if emp.balance > "5000"]
for emp in new_list :
  print(emp)
  print("-"*30)

# print costomer by who work as Software Engineer 
new_list = [emp for emp in New_Costomer.all_costomer if emp.job_title.lower() == "software engineer"]
for emp in new_list :
  print(emp)
  print("-"*30)

#print young costomers 
new_list = [emp for emp in New_Costomer.all_costomer if emp.age == "25"]
for emp in new_list :
  print(emp)
  print("-"*30)
