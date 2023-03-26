import sys

def organize(arg:str) -> str:
  """function used for organizing expression
    Args:
        arg (list): expression
    Returns:
        str: arg
    """
  arg = arg.replace(" ","")

  if "+" in arg:
    arg = arg.split("+")
    arg = ' + '.join(str(s) for s in arg)

  if "-" in arg:
    arg = arg.split("-")
    arg = ' - '.join(str(s) for s in arg)

  if "*" in arg:
    arg = arg .split("*")
    arg = ' * '.join(str(s) for s in arg)

  if "/" in arg:
    arg = arg.split("/")
    arg = ' / '.join(str(s) for s in arg)
  
  return arg

def check_expression(arg:str) -> bool:
  """function used for checking special symbols
    Args:
        arg (str): expression
    Returns:
        bool
    """
  if any(sym in arg for sym in '~!@#$%^&_`=,<>?:";\'\\|(){}[]ㄱ-힣'):
    return True
  
  return False

def isAdd(arg:list) -> bool:
  """function used for checking "+"
    Args:
        arg1 (list): expression
    Returns:
        bool
    """
  if "+" in arg:
    return True
  
  else: 
    return False
  
def isSubtract(arg:list) -> bool:
  """function used for checking "-"
    Args:
        arg1 (list): expression
    Returns:
        bool
    """
  if "-" in arg:
    return True
  
  else: 
    return False
  
def isMultiply(arg:list) -> bool:
  """function used for checking "*"
    Args:
        arg1 (list): expression
    Returns:
        bool
    """
  if "*" in arg:
    return True
  
  else: 
    return False
  
def isDivide(arg:list) -> bool:
  """function used for checking "/"
    Args:
        arg1 (list): expression
    Returns:
        bool
    """
  if "/" in arg:
    return True
  
  else: 
    return False
  

def add(arg1:list, arg2:int) -> list:
    """function used for adding two numbers
    Args:
        arg1 (list): expression
        arg2 (int) : index of expression
    Returns:
        list: arg1
    """
    if arg1[arg2] == "+":
      arg1[arg2] = float(arg1[arg2-1]) + float(arg1[arg2+1])
      del arg1[arg2-1], arg1[arg2]

      return arg1 # a calculated expression
    
    else: 
      add(arg1, arg2+1)

def subtract(arg1:list, arg2:int) -> list:
    """function used for substracting two numbers
    Args:
        arg1 (list): expression
        arg2 (int) : index of expression
    Returns:
        list: arg1
    """
    if arg1[arg2] == "-":
      arg1[arg2] = float(arg1[arg2-1]) - float(arg1[arg2+1])
      del arg1[arg2-1], arg1[arg2]

      return arg1 # a calculated expression
      
    else: 
      subtract(arg1, arg2+1)


def multiply(arg1:list, arg2:int) -> list:
    """function used for multiplying two numbers
    Args:
        arg1 (list): expression
        arg2 (int) : index of expression
    Returns:
        list: arg1
    """
    if arg1[arg2] == "*":
      arg1[arg2] = float(arg1[arg2-1]) * float(arg1[arg2+1])
      del arg1[arg2-1], arg1[arg2]

      return arg1 # a calculated expression
    
    else: 
      multiply(arg1, arg2+1)


def divide(arg1:list, arg2:int) -> list:
    """function used for dividing two numbers
    Args:
        arg1 (list): expression
        arg2 (int) : index of expression
    Returns:
        list: arg1
    """
    if arg1[arg2] == "/":
      arg1[arg2] = float(arg1[arg2-1]) / float(arg1[arg2+1])
      del arg1[arg2-1], arg1[arg2]

      return arg1 # a calculated expression

    else: 
      divide(arg1, arg2+1)

def calculation(arg1: list) -> list:
    """function used for calculation
    Args:
        arg1 (list): expression
    Returns:
        list: result
    """
    
    #check is there "*" in expression?
    if isMultiply(arg1):
      result = multiply(arg1, 0)

    #check is there "/" in expression?
    elif isDivide(arg1):
      result = divide(arg1, 0)

    #check is there "+" in expression?
    elif isAdd(arg1):
      result = add(arg1, 0)

    #check is there "-" in expression?
    elif isSubtract(arg1):
      result = subtract(arg1, 0)
    
    return result

def next_calculation():
  """function used for starting next calculation
    """
  while True:
    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Do next calculation? [y/n]: ")
    if next_calculation in ("y", "n"):
      if next_calculation == "y":
        break
        
      elif next_calculation == "n":
        sys.exit()
      
    else:
      print("Invalid Input")
      continue
      

if __name__ == "__main__":
  while True:
    expresion = input("Enter expression: ")
    expresion = organize(expresion)

    if check_expression(expresion):
      print("Invalid Input")
      next_calculation()
      continue

    expresion_list = expresion.split()


    while len(expresion_list) != 1:
        expresson_list = calculation(expresion_list)

    print(expresion + " = %f\n" %expresion_list[0])

    next_calculation()