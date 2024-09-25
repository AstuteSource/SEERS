"""Test suite to ensure that each function words correctly."""
import pytest
import os

from src import __version__
from src import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"

# calculate_area
def test_rectangle_area():
    assert main.calculate_area("rectangle",[2,3]) == 6

def test_circle_area():
    assert main.calculate_area("circle",[2]) == 12.56

def test_unsupported_shape():
    """Tests if an error is raised for unsupported shapes."""
    with pytest.raises(ValueError):
        main.calculate_area("square", [4])

# class User
def test_user_init_with_name_and_email():
    """Tests if User class initializes correctly with name and email."""
    user = main.User("Alice", "alice@example.com")
    assert user.name == "Alice"
    assert user.email == "alice@example.com"

# check_none
def test_check_none_with_none():
    """Tests if check_none returns True for None."""
    assert main.check_none(None) is True

def test_check_none_with_none():
    """Tests if check_none returns True for None."""
    assert main.check_none(None) is True

def test_check_none_with_value():
    """Tests if check_none returns False for a value."""
    assert main.check_none("data") is False

def test_check_none_with_zero():
    """Tests if check_none returns False for zero (falsy but not None)."""
    assert main.check_none(0) is False

def test_check_none_with_empty_string():
    """Tests if check_none returns False for an empty string (falsy but not None)."""
    assert main.check_none("") is False

# handle_file
def test_handle_file_success(tmp_path):
    """Tests if handle_file reads a file successfully."""
    # Create a temporary file with some content
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("This is some test data.")
    main.handle_file(str(test_file))
    with open(str(test_file)) as f:
        assert f.read() == "This is some test data."

# is_valid
def test_is_valid_true():
    """Tests if is_valid returns 'true value' for True."""
    assert main.is_valid(True) == "true value"

def test_is_valid_false():
    """Tests if is_valid returns 'false value' for False."""
    assert main.is_valid(False) == "false value"

# get_user_data
def test_get_user_data():
    """Tests if get_user_data returns a user's name."""
    user_data = {"name": "Alice", "name":"Bob"}
    name = main.get_user_data(user_data)
    assert name in ("Alice", "Bob")

def test_get_user_data_without_name():
    """Tests if get_user_data returns None when 'name' is missing."""
    user_data = {"email": "alice@example.com"}
    assert main.get_user_data(user_data) is None

def test_get_user_data_empty_dict():
    """Tests if get_user_data returns None for an empty dictionary."""
    assert main.get_user_data({}) is None

# validate_data
def test_validate_data_with_tuple():
    """Tests if validate_data passes with a tuple."""
    data = (1, 2, 3)
    main.validate_data(data)

def test_validate_data_with_non_tuple():
    """Tests if validate_data raises an AssertionError for non-tuple data."""
    with pytest.raises(AssertionError):
        main.validate_data([1, 2, 3])

def test_validate_data_with_none():
    """Tests if validate_data raises an AssertionError for None."""
    with pytest.raises(AssertionError):
        main.validate_data(None)

# modify_list
def test_modify_list():
    """Tests if modify_list modifies a copy of the list and returns it."""
    original_data = [1, 2, 3]
    modified_data = main.modify_list(original_data)
    assert modified_data == ["Modified", "Modified", "Modified"]
    assert original_data == [1, 2, 3]

# calculate_sum
def test_calculate_sum_empty():
    """Tests if calculate_sum returns 0 for an empty list."""
    assert main.calculate_sum([]) == 0

def test_calculate_sum_positive():
    """Tests if calculate_sum returns the correct sum for positive numbers."""
    assert main.calculate_sum([1, 2, 3]) == 6

def test_calculate_sum_negative():
    """Tests if calculate_sum returns the correct sum for negative numbers."""
    assert main.calculate_sum([-1, -2, -3]) == -6

def test_calculate_sum_mixed():
    """Tests if calculate_sum returns the correct sum for mixed numbers."""
    assert main.calculate_sum([1, -2, 3]) == 2

# handle_request
def test_handle_get_request():
    """Tests if handle_request returns the correct message for a GET request."""
    assert main.handle_request("GET", None) == "Processing GET request"

def test_handle_post_request_with_data():
    """Tests if handle_request returns the correct message for a POST request with data."""
    assert main.handle_request("POST", {"data": "value"}) == "Processing POST request with data"

def test_handle_post_request_without_data():
    """Tests if handle_request returns the correct message for a POST request without data."""
    assert main.handle_request("POST", None) == "Processing POST request without data"

def test_handle_unsupported_method():
    """Tests if handle_request returns the correct message for an unsupported method."""
    assert main.handle_request("PUT", None) == "Unsupported method"

# filter_data
def test_filter_data_with_condition_and_data():
    """Tests if filter_data returns all non-None elements with a True condition."""
    data = [1, None, "hello", 2.5]
    condition = True
    filtered_data = main.filter_data(data, condition)
    assert filtered_data == [1, "hello", 2.5]

def test_filter_data_with_condition_and_no_data():
    """Tests if filter_data returns an empty list with a True condition and empty data."""
    data = []
    condition = True
    filtered_data = main.filter_data(data, condition)
    assert filtered_data == []

def test_filter_data_with_false_condition():
    """Tests if filter_data returns an empty list with a False condition."""
    data = [1, None, "hello", 2.5]
    condition = False
    filtered_data = main.filter_data(data, condition)
    assert filtered_data == []

def test_filter_data_with_all_none():
    """Tests if filter_data returns an empty list with all None elements."""
    data = [None, None, None]
    condition = True
    filtered_data = main.filter_data(data, condition)
    assert filtered_data == []

# classify_number
def test_classify_positive_number():
    """Tests if classify_number returns 'Positive number' for a positive number less than 100."""
    assert main.classify_number(50) == "Positive number"

def test_classify_large_positive_number():
    """Tests if classify_number returns 'Large positive number' for a number greater than 100."""
    assert main.classify_number(120) == "Large positive number"

def test_classify_negative_number():
    """Tests if classify_number returns 'Negative number' for a negative number."""
    assert main.classify_number(-30) == "Negative number"

def test_classify_zero():
    """Tests if classify_number returns 'Zero' for zero."""
    assert main.classify_number(0) == "Zero"

# calculate_factorial
def test_factorial_zero():
    """Tests if calculate_factorial returns 1 for factorial of 0."""
    assert main.calculate_factorial(0) == 1

def test_factorial_negative():
    """Tests if calculate_factorial raises an error for a negative number."""
    with pytest.raises(ValueError):
        main.calculate_factorial(-3)

def test_factorial_custom_start():
    """Tests if calculate_factorial returns the correct factorial with a custom starting value."""
    assert main.calculate_factorial(3, start=2) == 12

#validate_user_input
def test_valid_user_input():
    """Tests if validate_user_input returns True for valid name and email."""
    assert main.validate_user_input("Alice", "alice@example.com") is True

def test_invalid_name_with_numbers():
    """Tests if validate_user_input raises an AssertionError for name with numbers."""
    with pytest.raises(AssertionError):
        main.validate_user_input("Alice123", "alice@example.com")

def test_invalid_name_with_symbols():
    """Tests if validate_user_input raises an AssertionError for name with symbols."""
    with pytest.raises(AssertionError):
        main.validate_user_input("Alice!", "alice@example.com")

def test_invalid_email_without_at():
    """Tests if validate_user_input raises an AssertionError for email without '@'."""
    with pytest.raises(AssertionError):
        main.validate_user_input("Alice", "alice.example.com")

#write_to_file
def test_write_to_file_content(tmpdir):
    """Tests if the written data is present in the file (using a temporary directory)."""
    data = "This is some test data."
    filename = os.path.join(tmpdir, "test_file.txt")
    main.write_to_file(filename, data)
    with open(filename, "r") as f:
        written_data = f.read()
    assert written_data == data

#calculate_grade
def test_grade_a():
    """Tests if calculate_grade returns 'A' for a score above or equal to 90."""
    assert main.calculate_grade(90) == "A"
    assert main.calculate_grade(100) == "A"

def test_grade_b():
    """Tests if calculate_grade returns 'B' for a score between 80 (inclusive) and 89 (exclusive)."""
    assert main.calculate_grade(80) == "B"
    assert main.calculate_grade(89) == "B"

def test_grade_c():
    """Tests if calculate_grade returns 'C' for a score between 70 (inclusive) and 79 (exclusive)."""
    assert main.calculate_grade(70) == "C"
    assert main.calculate_grade(79) == "C"

def test_grade_f():
    """Tests if calculate_grade returns 'F' for a score below 70."""
    assert main.calculate_grade(69) == "F"
    assert main.calculate_grade(0) == "F"

#calculate_discount
def test_no_discount_no_loyalty():
    """Tests if calculate_discount returns the original price without discount or loyalty points."""
    price = 100
    discount_rate = 0
    loyalty_points = 0
    assert main.calculate_discount(price, discount_rate, loyalty_points) == price

def test_with_discount_no_loyalty():
    """Tests if calculate_discount applies the discount correctly without loyalty points."""
    price = 100
    discount_rate = 0.1  # 10% discount
    loyalty_points = 0
    expected_price = price - (price * discount_rate) - ((price * discount_rate) * 0.1)
    assert main.calculate_discount(price, discount_rate, loyalty_points) == expected_price

def test_with_discount_and_loyalty():
    """Tests if calculate_discount applies both discount and loyalty bonus."""
    price = 100
    discount_rate = 0.1  # 10% discount
    loyalty_points = 150
    expected_price = price - (price * discount_rate) - ((price * discount_rate) * 0.1) - (price * 0.05)
    assert main.calculate_discount(price, discount_rate, loyalty_points) == expected_price

def test_edge_case_loyalty_points():
    """Tests if calculate_discount handles loyalty points exactly at the threshold (100)."""
    price = 100
    discount_rate = 0.1  # 10% discount
    loyalty_points = 100
    expected_price = price - (price * discount_rate) - ((price * discount_rate) * 0.1)
    assert main.calculate_discount(price, discount_rate, loyalty_points) == expected_price

#overly_complex_function
def test_valid_item_above_min_order():
    """Tests if the function filters an item above min_order_value and applies discount."""
    data = [
        {'id': 1, 'value1': 15, 'value2': 3, 'price': 120},
    ]
    filtered_data = main.overly_complex_function(data)
    assert len(filtered_data) == 1
    assert filtered_data[0]['discounted_price'] == 108  # Discount applied

def test_valid_item_with_loyalty_discount():
    """Tests if the function applies loyalty discount for high loyalty_points."""
    data = [
        {'id': 1, 'value1': 15, 'value2': 3, 'price': 120},
    ]
    filtered_data = main.overly_complex_function(data, loyalty_points=120)
    assert len(filtered_data) == 1
    assert filtered_data[0]['discounted_price'] == 102

#class Person
def test_odd_even_valid_input():
    person = main.Person()
    assert person.odd_even(0) == "even"
    assert person.odd_even(1) == "odd"
    assert person.odd_even(10) == "even"

def test_odd_even_invalid_input():
    person = main.Person()
    assert person.odd_even(-1) == "Invalid age"