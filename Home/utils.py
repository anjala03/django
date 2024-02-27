from Home.models import Author
import time
def a_func_exe():
    #this cannot acess the model named Author until shell is used
    print("Function started")
    time.sleep(2)
    print("function terminated")
    #from shell this is imported and then the functoon is called then only it will run 