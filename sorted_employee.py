"""
Sorted Employee

Created by Jas Lau on 7/9/19.
Copyright © 2019 Jas Lau. All rights reserved.

"""
import copy
import numpy
import random
from enum import Enum


# ============================= Global Functions =============================


def print_array(arr):
    """Print all Employee objects
    Args:
        arr: employee array

    Returns: None

    """
    for i in range(array_size):
        print(i + 1, ".)", arr[i])


def float_largest_to_top(arr):
    """Insertion sort to sort the arr from largest to smallest.
    Args:
        arr: unsorted old array

    Returns: new sorted array

    """
    for i in range(array_size):
        current_obj = arr[i]
        pos = i - 1
        # if current > previous
        while pos >= 0 and current_obj.employee_num > arr[pos].employee_num:
            # swap
            arr[pos + 1] = arr[pos]
            pos -= 1
        # elif it is in order
        arr[pos + 1] = current_obj
    return arr


def binary_search_for_id(arr, target):
    """Iterative Implementation of Binary Search. It return the index of
    target in given array if present, else, return None.
    Args:
        arr:
        target:

    Returns:

    """
    for i in range(array_size):
        left_index, right_index = 0, len(arr) - 1
        while left_index <= right_index:
            middle_index = int(left_index + right_index) // 2
            # If target is on the left side of middle position
            if arr[middle_index].employee_num > target:
                left_index = middle_index + 1
            # If target is on the right side of middle position
            elif target > arr[middle_index].employee_num:
                right_index = middle_index - 1
            # else target is in middle position
            else:
                return middle_index
        return None


# ========================== End Of Global Functions =========================

# ========================== Client As Main Functions ========================


def main():
    # Test
    print("Employee array size: ", array_size)
    print("\n----- Unsorted Employee List -----")
    arr1 = employee_arr
    print_array(arr1)
    print("\n----- Sorted Employee List (Largest on Top) -----\n")
    sorted_obj = float_largest_to_top(arr1)
    print_array(arr1)

    print("\n----- Search for employee number -----\n")

    # Create a Queue
    s1 = MyQueue()

    # Ask user for input
    user_input = 0
    while user_input != 7:
        try:
            user_input = int(input("Please pick an employee number from the "
                                   "display (Press 7 to quit): "))
        except ValueError:
            print("Please enter number only!")
            continue
        else:
            target_index = binary_search_for_id(sorted_obj, user_input)
            if target_index is None and target_index != 7 and \
                    target_index != 1 and target_index != 2:
                print("Employee number not found!")
                continue
            s1.enqueue(str(sorted_obj[target_index]))
            user_choice = int(input("Do you want to continue (Press 1 for "
                                    "YES, 2 for NO)? "))
            if user_choice == 1:
                continue
            else:
                break

    print("\n--------- The Queue ---------\n")
    MyQueue.show(s1)
    print("\n--------- Dequeue ---------\n")
    for k in range(0, 10):
        print("[" + str(s1.dequeue()) + "]")


# ======================= End Of Client As Main Functions ====================

# =============================== Queue Class ================================


class MyQueue:
    """Create a numpy array of employee objects."""
    # static members and intended constant
    MAX_SIZE = 100000
    DEFAULT_SIZE = 10
    EMPTY_QUEUE_RETURN_ALERT = "** attempt to remove from empty queue **"
    ORIG_DEFAULT_ITEM = ""
    default_item = ORIG_DEFAULT_ITEM

    # constructor
    def __init__(self, size=DEFAULT_SIZE, default_item=None):
        self.front = 0
        self.rear = size - 1
        self.q = []
        # instance attributes
        self.capacity = size

        # initialize an array of size=capacity for our queue, all to
        # default_item
        if default_item is not None:
            self.default_item = default_item

        # force queue to be empty by setting self.front to 0
        self.clear()

    def __str__(self):
        ret_str = Employee.to_string()
        return ret_str

    # accessors
    @property
    def capacity(self):
        return self.size

    # mutators
    @capacity.setter
    def capacity(self, size):
        if not MyQueue.valid_capacity(size):
            self.size = MyQueue.DEFAULT_SIZE
        else:
            self.size = size
            self.clear()

    def enqueue(self, item_to_add):
        # if full
        if self.front == self.size:
            print("The queue is full!")
            return False
        elif not isinstance(item_to_add, str):
            return False
        else:
            self.q[self.rear] = item_to_add
            self.rear = (self.rear + 1) % self.size
            self.front += 1
            return True

    def dequeue(self):
        # if empty
        if self.front == 0:
            return self.EMPTY_QUEUE_RETURN_ALERT
        # else
        self.front -= 1
        return self.q.pop(0)

    def clear(self):
        """  remove all items from queue """
        # deepcopy() for mutable defaults - details later
        self.q = [copy.deepcopy(self.default_item) for k in
                  range(self.size)]
        self.front = 0
        self.rear = 0

    def show(self):
        for i in range(self.front):
            print(self.q[i])

    # static/class methods ------------------------
    @classmethod
    def valid_capacity(cls, test_capacity):
        if not (0 <= test_capacity <= cls.MAX_SIZE):
            return False
        else:
            return True

    @classmethod
    def set_default_item(cls, new_default):
        """ this will change the default of newly instantiated queues """
        cls.default_item = new_default

    def float_largest_to_top(arr):
        """Insertion sort to sort the arr from largest to smallest.
        Args:
            arr: unsorted old array

        Returns: new sorted array

        """
        for i in range(array_size):
            current_obj = arr[i]
            pos = i - 1
            # if current > previous
            while pos >= 0 and current_obj.employee_num > arr[pos].employee_num:
                # swap
                arr[pos + 1] = arr[pos]
                pos -= 1
            # elif it is in order
            arr[pos + 1] = current_obj
        return arr


# ========================== End Of Queue Class ==============================


class EmpNumError(Exception):
    pass


# ============================ Employee Class ================================


class Shift(Enum):
    DAY = 1
    SWING = 2
    NIGHT = 3

    def __str__(self):
        ret_str = self.name.capitalize()
        return ret_str


class Employee:
    # static member
    DEFAULT_NAME = "unidentified"
    DEFAULT_NUM = 1234
    DEFAULT_SHIFT = Shift.DAY
    BENEFIT_ID = 5000
    MIN_EMPLY_NUM = 1000
    MAX_EMPLY_NUM = 99999

    # constructor
    def __init__(self, name, number, shift):
        self.employee_name = name
        self.employee_num = number
        self.employee_shift = shift

    # accessors
    @property
    def employee_name(self):
        return self.__name

    @property
    def employee_num(self):
        return self.__number

    @property
    def employee_shift(self):
        return self.__shift

    def get_determine_benefits(self):
        return self.__benefits

    # mutators
    @employee_name.setter
    def employee_name(self, name):
        """Set the employee name.

        Args:
            name (str): Employee name
        """
        if self.validate_name(name):
            self.__name = name
        else:
            self.__name = self.DEFAULT_NAME

    @employee_num.setter
    def employee_num(self, number):
        """Set employee's number. This method will call determine_benefits().
           - benefits (bool): Hold the boolean value of the employee benefits.

        Args:
            number (int): Employee id

        Returns:
            self.number = self.DEFAULT_NUM
        """
        if self.validate_id(number):
            self.__number = number
        else:
            self.__number = self.DEFAULT_NUM

        if self.determine_benefits(number):
            self.__benefits = True
        else:
            self.__benefits = False

    @employee_shift.setter
    def employee_shift(self, shift):
        """ Set employee shift.

        Args:
            shift (Enum): Employee shift.

        Returns:
            Shift: Set instance variable shift to input shift if valid. Set to default shift otherwise.
        """
        if isinstance(shift, Shift):
            self.__shift = shift
        elif type(shift) is int and (1 <= shift <= 3):
            self.__shift = Shift(shift)
        else:
            self.__shift = self.DEFAULT_SHIFT

    # helper function
    def __str__(self):
        """Print employees' information in format:
           'Name #id (Benefits) Shift: DAY.'

        Returns:
            str: Return a string.
        """
        if self.get_determine_benefits():
            ret_str_bnft = "Benefits"
        else:
            ret_str_bnft = "No Benefits"

        ret_str = '{} | ID #: {} | (*{})\nShift: {}'.format(self.employee_name,
                                                            str(self.employee_num), ret_str_bnft,
                                                            self.employee_shift)
        return ret_str

    def determine_benefits(self, number):
        """Determine if an employee can get benefits.

        Args:
            number (int): Employee id

        Returns:
            bool: True for eligible. False otherwise.
        """
        return number < Employee.BENEFIT_ID

    @classmethod
    def validate_name(cls, the_name):
        """Check if the input employee name is valid.

        Args:
            the_name (str): Employee name

        Returns:
            bool: True for valid. False otherwise.
        """
        return type(the_name) is str and the_name.isnumeric() is False

    @classmethod
    def validate_id(cls, employee_id):
        """Check if the input employee id is valid and if it is in range.

        Args:
            employee_id (int): Employee id

        Returns:
            bool: True for valid. False otherwise.
        """
        return (type(employee_id) is int and
                Employee.MIN_EMPLY_NUM <= employee_id <= Employee.MAX_EMPLY_NUM)


# ========================= End Of Employee Class ============================

# List of Names
name_list = ["Vickie Mclaughlin", "Maryrose Hoffman", "Chantel Cantrell",
             "Andy Farrell", "Roselle Lambert", "Shizuko Woodard",
             "Nada Castillo", "Myrle Dougherty", "Leeanna Keith",
             "Millard Colon"]

# List Comprehension of Employee Objects
employee_arr = numpy.array(
    [Employee(n, random.randint(1000, 10000), random.randint(1, 4)) for n in
     name_list])
array_size = len(employee_arr)

if __name__ == "__main__":
    main()
