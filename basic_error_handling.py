

##################################### Basic Error Handling #####################################
# Description: This code attempts to divide no_2 by no_1, which is zero, causing a division by zero error. 
# Since there is no error handling, this will raise an exception and stop execution.

no_1 = 0
no_2 = 5
ans = no_2 / no_1  # This line causes a ZeroDivisionError
print("OK ")


###################################### Basic Try-Except Block #####################################
# Description: This code uses a try-except block to handle any errors that occur during execution. 
# If an error occurs, it prints "Exception occurred".

try:
    no_1 = 0
    no_2 = 5
    ans = no_2 / no_1  # This line causes a ZeroDivisionError
    print("OK ")
except:
    print("Exception occurred")  # Catch all exceptions


##################################### Try-Except with Exception Details #####################################
# Description: This code catches all exceptions and prints the error message before indicating an exception occurred.

try:
    no_1 = 0
    no_2 = 5
    ans = no_2 / no_1  # This line causes a ZeroDivisionError
    print("OK ")
except Exception as Err:
    print(Err)  # Print the error message
    print("Exception occurred")  # Catch all exceptions


###################################### Specific Exception Handling #####################################
# Description: This code specifically handles ZeroDivisionError, indicating when a division by zero occurs.

try:
    no_1 = 0
    no_2 = 5
    ans = no_2 / no_1  # This line causes a ZeroDivisionError
    print("OK ")
except ZeroDivisionError:
    print("Exception occurred")  # Catch division by zero error


###################################### Multiple Specific Exception Handling #####################################
# Description: This code handles both ZeroDivisionError and NameError separately, printing different messages for each.

try:
    no_1 = 0
    no_2 = 5
    ans = no_2 / no_1  # This line causes a ZeroDivisionError
    print("OK ")
except ZeroDivisionError:
    print("Zero division error occurred")  # Catch division by zero error
except NameError:
    print("Name error occurred")  # Catch undefined variable error


# Description: This code will cause a NameError because no_1_1 is not defined.

try:
    no_1 = 0
    no_2 = 5
    ans = no_2 / no_1_1  # This line causes a NameError
    print("OK ")
except ZeroDivisionError:
    print("Zero division error occurred")  # Catch division by zero error
except NameError:
    print("Name error occurred")  # Catch undefined variable error


####################################### Finally Block ######################################
# Description: This code demonstrates the use of a finally block, 
# which always executes, regardless of whether an exception occurred or not.

try:
    no_1 = 0
    no_2 = 5
    ans = no_2 / no_1  # This line causes a ZeroDivisionError
    print("OK ")
except ZeroDivisionError:
    print("Zero division error occurred")  # Catch division by zero error
except NameError:
    print("Name error occurred")  # Catch undefined variable error
finally:
    print("Finally block reached")
    a = 5
    b = 4
    c = a * b
    print(c)  # This will always execute


####################################### Correct Division and Finally Block ######################################
# Description: This code performs a valid division and includes a finally block.

try:
    no_1 = 0
    no_2 = 5
    ans = no_1 / no_2  # This line does not cause an error
    print("OK ")
except ZeroDivisionError:
    print("Zero division error occurred")  # Catch division by zero error
except NameError:
    print("Name error occurred")  # Catch undefined variable error
finally:
    print("Finally block reached")
    a = 5
    b = 4
    c = a * b
    print(c)  # This will always execute


####################################### Else Block ######################################
# Description: This code uses an else block, which executes only if no exceptions occur.

try:
    no_1 = 0
    no_2 = 5
    ans = no_1 / no_2_2  # This line causes a NameError
    print("OK ")
except ZeroDivisionError:
    print("Zero division error occurred")  # Catch division by zero error
except NameError:
    print("Name error occurred")  # Catch undefined variable error
else:
    print("All done")  # Executes if no exceptions occur
finally:
    print("Finally block reached")
    a = 5
    b = 4
    c = a * b
    print(c)  # This will always execute


####################################### Comprehensive Error Handling ######################################
# Description: This code handles multiple specific exceptions and includes an else and finally block.

try:
    no_1 = 0
    no_2 = 5
    ans = no_1 / no_2  # This line does not cause an error
    print("OK ")
except ZeroDivisionError:
    print("Zero division error occurred")  # Catch division by zero error
except NameError:
    print("Name error occurred")  # Catch undefined variable error
except Exception as Err:
    print(Err)  # Catch any other exceptions
else:
    print("All done")  # Executes if no exceptions occur
finally:
    print("Finally block reached")
    a = 5
    b = 4
    c = a * b
    print(c)  # This will always execute
    

####################################### Key Error Handling ######################################
# Description: This code attempts to access a non-existent key in a dictionary, causing a KeyError.

try:
    temp_dictionary = {"shra": 100, "Sah": 100, "Jay": 100}
    print(temp_dictionary["shra"])  # This line works
    print(temp_dictionary["shraaa"])  # This line causes a KeyError
except KeyError:
    print("Key error occurred")  # Catch key access error
