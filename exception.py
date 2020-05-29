def divide():
    
    try:
        #print("enter two numbers")
        x = int(input("enter divident : "))
        y = int(input("enter divisor : "))
        q  = x / y
        rem = x%y
    except ZeroDivisionError:
        print("division by zero !")
    except TypeError:
        print("you might have entered a string")
    except ValueError:
        print("enter a int please")
    except KeyboardInterrupt:
        print("you cancelled the operation")
    else:
        print("quotient is " + str(q) + "  &  remainder is " + str(rem)) 

if __name__ == "__main__" :

    divide()         
