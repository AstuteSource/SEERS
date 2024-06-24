""" Config Checks Project. """
from typing import Tuple

def calculate_area(shape,dimensions):
    """This function calculates the area of a shape based on its dimensions.

    Contains Patterns:
        - Double Nested If (DNI)
        - Magic Number (MN)
        - No exception type (EXC)
        - Missing type annotation (ANNOT)
        - Unused Variables (UNUSED)
    """
    if shape == "rectangle":
        area = dimensions[0] * dimensions[1]
        return area
    else:
        if shape == "circle":
            radius = dimensions[0]
            return 3.14 * dimensions[0] ** 2
        else:
            raise ValueError("Unsupported shape")

class User:
    """This class represents a user with a name and email address.

    Contains Patterns:
        - Explicit Return in __init__(RET)
    """
    def __init__(self,name,email):
        self.name = name
        self.email = email
        return

# TODO: Not passing pattern check id: 'NONE001', name: 'none-comparison'
def check_none(value):
    """This function checks if a value is None.

    Contains Pattern:
        - none comparision (NONE)
    """
    if value is not None:
        return False
    return True

# TODO: Not passing check id: 'EXC001', name: 'no-exception-type', pattern: './/FunctionDef//Try/ExceptHandler[not(ExceptHandler/type)]'
def handle_file(filename):
    """
    This function attempts to read a file but does not handle specific exception

    Contains Patterns:
        - No Exception type (EXC)
    """
    try:
        with open(filename) as f:
            data = f.read()
    except IOError as e:
        print(f"Error reading file: {e}")

def is_valid(value):
    """
    This function checks if a value is true.

    Contains Patterns:
        - Boolean Comparison (BOOL)
    """
    if value is True:
        return "true value"
    else:
        return "false value"

# TODO: not passing check id: 'MVKL001', name: 'multi-value-key-literal', pattern: './/FunctionDef/body/Assign/value/Dict/keys/Name[preceding-sibling::Name/@id= @id]
def get_user_data(user_data):
    """
    This function retrieves a user's name from a dictionary using the keys() function

    Contains Patterns:
        - Key Function (KFUN)
        - Single Nested If (SNI)
        - Multi-value key literal (MVKL)
    """
    if "name" in user_data.keys():
        return user_data["name"]
    else:
        return None


# Multi-value key literal (MVKL)- outside function scope
user_data = {"name": "Alice", "name":"Bob"}

# TODO: not passing check id: 'AT001', name: 'assert-tuple', pattern: './/FunctionDef[./body/Assert/test/Tuple]'
def validate_data(data):
    """ Asserts on tuple.
        Contains Patterns:
        - Assertion (AT)
    """
    assert type(data) == tuple, "Data must be a tuple"

# TODO: not passing check id: 'LVITOI001', name: 'loop-variable-iterates-overrides-iterator', pattern: './/FunctionDef/body/For[target/Name/@id = iter/Name/@id]'
def modify_list(data):
    """
    This function modifies a list by overiding its elements.

    Contains Patterns:
    - Loop variable iterates and overrides iterator (LVITOI)
    """
    modified_data = []
    for item in data:
        item = "Modified"
        modified_data.append(item)
    return modified_data

# TODO: id: 'FLV001', name: 'function-uses-loop-variable', pattern: './/FunctionDef[body//comprehension/target/Name]'
def calculate_sum(numbers):
    """
    This function calculate the sum of a integer list

    Contains Patterns:
        - Function using loop variable (FLV)"""
    total = 0
    for num in numbers:
        total += num
    return total

def nested_function_1():
    """ Function with nested depth (ND)"""
    def nested_function_2():
        def nested_function_3():
            pass
    nested_function_2()

def handle_request(method, data):
    """Function with multiple conditions (COND) and count method lines (CML)"""
    if method == "GET":
        return "Processing GET request"
    elif method == "POST":
        if data is not None:
            return "Processing POST request with data"
        else:
            return "Processing POST request without data"
    else:
        return "Unsupported method"

# TODO: not passing check id: 'CL002', name: 'nested-condition-loops', pattern: './/FunctionDef//if//For'
def filter_data(data, condition):
    """Function with nested condition-loop if{for{}} (IFOR) and (VFF) for{if{}}"""
    filtered_data = []
    if condition:
        for item in data:
            if item is not None:
                filtered_data.append(item)
    return filtered_data

def classify_number(number):
    """
    This function classifies a number as positive, negative, or zero.

    Contains Patterns:
    - Nested condition (IFIF)
    """
    if number > 0:
        if number > 100:
            return "Large positive number"
        else:
            return "Positive number"
    else:
        if number < 0:
            return "Negative number"
        else:
            return "Zero"

def calculate_factorial(n, start=1):
    """
    This function calculates the factorial of a number n, optionally starting from a specific value.

    Contains Pattern: Nested Loop-Conditions (FF) for{for{}}
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    factorial = 1
    for i in range(start, n + 1):
        for j in range(2, i + 1):
            factorial *= j
    return factorial

def validate_user_input(name, email):
    """
    This function validates user input for name and email. (Simple example)

    Contains Pattern: Number of Assertions (NOA)
    """
    assert name.isalpha(), "Name must only contain letters"
    assert "@" in email, "Email must contain an '@' symbol"
    return True

# TODO: not passing check id: 'DUCM001', name: 'not-using-context-manager', pattern: './/FunctionDef//*[starts-with(., "with open")]'
def write_to_file(filename, data):
    """
    This function writes data to a file without using a context manager.

    Contains Pattern: Not Using Context Manager (DUCM)
    """
    with open(filename, "w") as f:
        f.write(data)

def calculate_grade(score):
    """
    This function calculates a letter grade based on a score. (Simple example)

    Contains Pattern: Multiple Returns in Function (MRET)
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        if score >= 70:
            return "C"
        else:
            return "F"

# TODO: id: 'COMPLEX001', name: 'complex-expressions', pattern: './/FunctionDef//BinOp[count(descendant::BinOp) > 2]
def calculate_discount(price, discount_rate, loyalty_points):
    """
    This function calculates a discounted price with complex logic.

    Contains Pattern: Complex Expressions (COMPLEX)
    """
    discount = price * discount_rate
    final_price = price - discount - (discount * 0.1)
    if loyalty_points > 100:
        final_price -= price * 0.05
    return final_price

# JSS paper

def overly_complex_function(data, threshold1=10, threshold2=5, discount_rate=0.1, loyalty_points=0, min_order_value=100, global_variable=1):
    """
    This function demonstrates a combination of code smells for demonstration purposes.

    Contains Patterns:
        - High Cyclomatic Complexity (HCC): Uses multiple nested conditionals.
        - Long Parameter List (LPL): Has 7 parameters.
        - Deeply Nested Control Structures (DNCS): Uses nested ifs and fors.
        - Magic Numbers: Uses hardcoded values (thresholds, discount rate).
    """
    filtered_data = []

    for item in data:
        if item['value1'] > threshold1 and item['value2'] < threshold2:
            if item['price'] > min_order_value:
                discount = item['price'] * discount_rate
                if loyalty_points > 100:
                    discount += item['price'] * 0.05 
                item['discounted_price'] = item['price'] - discount
                filtered_data.append(item)
            else:
                print(f"Order value for item {item['id']} is below minimum ({min_order_value})")
        else:
            print(f"Item {item['id']} does not meet the value thresholds")
        pass

    # Deeply nested control structures (can be further nested for DNCS)
    if len(filtered_data) > 0:
        for item in filtered_data:
            if item['discounted_price'] < 0:
                item['discounted_price'] = 0
        global_variable += 1
    else:
        print("No items met the filtering criteria.")

    return filtered_data

class Person:
    """A complex class
    Contains Patterns:
        - God Object (GO): Has many responsibilities.
        - Large Class (LC)
        - Long method chaining (LMC)
        - Include empty catch block (ECB)
        - Long Scope Chaining (LSC)
        - Number of Conditions in Function (COND)
    """
    def __init__(self, name="", age= 0, ssn=None, email="", address = ""):
        self.name = name
        self.age = age
        self.ssn = ssn
        self.email = email
        self.address = address
    def setName(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        # Simulate unnecessary validation logic (for LM)
        for char in name:
            if not char.isalpha() and not char.isspace():
                raise ValueError("Name can only contain letters and spaces")
        self.name = name
        return self
    def setAge(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        try:
            self.age = int(age)  # Potential for type conversion errors
        except ValueError:
            pass  # Empty catch block (ECB)
    def setSSN(self, ssn):
        self.ssn = ssn
        return self
    def setEmail(self,email):
        self.email = email
        return self
    def setAddress(self,address):
        self.address = address
        return self
    def create_person():
        p = Person()
        p.setName("John").setAge(30).setSSN("123-45-678").setEmail("johndoe@gmail.com").setAddress("123Street")
        return p
    def validate_ssn(self):
        if not self.ssn:
            return False
        if len(self.ssn) != 11:
            return False
        parts = self.ssn.split("-")
        if len(parts) != 3:
            return False
        try:
            int(parts[0])
            int(parts[1])
            int(parts[2])
        except ValueError:
            return False
        return True
    def odd_even(self,age):
        if age >= 0:
            if age == 0:
                return "even"
            elif age == 1:
                return "odd"
            elif age == 2:
                return "even"
            elif age == 3:
                return "odd"
            elif age == 4:
                return "even"
            elif age == 5:
                return "odd"
            elif age == 6:
                return "even"
            elif age == 7:
                return "odd"
            elif age == 8:
                return "even"
            elif age == 9:
                return "odd"
            elif age == 10:
                return "even"
            elif age == 11:
                return "odd"
            elif age == 12:
                return "even"
            elif age == 13:
                return "odd"
            elif age == 14:
                return "even"
            elif age == 15:
                return "odd"
            elif age == 16:
                return "even"
            elif age == 17:
                return "odd"
            elif age == 18:
                return "even"
            elif age == 19:
                return "odd"
            elif age == 20:
                return "even"
            elif age == 21:
                return "odd"
            elif age == 22:
                return "even"
            elif age == 23:
                return "odd"
            elif age == 24:
                return "even"
            elif age == 25:
                return "odd"
        else:
            return "Invalid age"


global_var = 0  # This is a global variable

def calculate_something(data):
    """
    This function demonstrates the use of a global variable.

    Contains Pattern (and code smell):
        - Use of Global Variables (UGV): Uses a global variable 'global_var'.
    """
    result = data['field1'] * data['field2'] * 2
    global_var += 1  # Modifying global variable
    return result + global_var
