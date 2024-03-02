from abc import ABC,abstractmethod
class BankingApp:
    def database(self):
        print(f"Connect to Database Sucessfully")
    def security(self):
        print("security of mobile app")

class MobileApp(BankingApp):
    def login_app(self):
        print("Login Sucessfully")

if __name__ =="main":
    bank =BankingApp()
    bank.database()