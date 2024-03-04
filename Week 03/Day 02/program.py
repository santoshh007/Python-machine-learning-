class  Error (Exception):
    pass
class DobException(Error):
    pass
user_age=int(input("Enter your valid age",))
try:
    if  user_age<=3 and user_age>20:
        print("You are valid for this program")
    else:
        raise DobException
except DobException:
    print("Sorry,please pass valid age")