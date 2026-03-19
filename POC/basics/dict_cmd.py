std_dict = {"name": "John", "age": 30, "city": "New York"}
print(std_dict)
print(std_dict["name"])
# Use dict.get() to avoid KeyError and provide a default value when key is missing
print(std_dict.get("country", "Unknown"))
# Update values by assigning directly to keys (existing or new)
std_dict["age"] = 24
std_dict["graduated"] = False
print(std_dict)
# Another way: update multiple key/value pairs at once
# std_dict.update({"age": 24, "graduated": False})
std_dict.update({"hobbies": ["reading", "traveling"]})
print(std_dict)
del std_dict["city"]
print(std_dict)

# Iterate over keys
for key in std_dict:
    print(key)

# Iterate over values
for value in std_dict.values():
    print(value)

# Iterate over key/value pairs
for key, value in std_dict.items():
    print(f"{key}: {value}")

print(list(std_dict.items()))

# Simple helper: check if a key exists in a dict
# Returns True if present, False otherwise

def key_exists(d: dict, key) -> bool:
    return key in d

print(key_exists(std_dict, "name"))    # True
print(key_exists(std_dict, "country")) # False

print(std_dict.get("country", "Unknown")) # "Unknown"
print(std_dict.get("name", "Unknown"))    # "John"

d = {"a": 1, "b": 2}
d.setdefault("c", 3)  # Adds "c": 3 since "c" is not already a key
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
d.setdefault("a", 10) # Does not change "a" since "a" is already a key
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}

squares = {x: x**2 for x in range(5)}
print(squares)  

squaresFilter = {x: x**2 for x in range(5) if x % 2 == 0}
print(squaresFilter)

directory = {
    "folder1": {
        "file1": 123,  # size in bytes
        "file2": 456
    },
    "folder2": {
        "file3": 789
    }
}

file2_size = directory["folder1"]["file2"]
print(file2_size)  # Output: 456

#safe access 
file2_size_safe = directory.get("folder1", {}).get("file2", "File not found")
print(file2_size_safe)  # Output: 456

e = {"a": 1, "b": 2}
f = {"b": 3, "c": 4}
merged = {**e, **f}  # Merges e and f, with f
print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}

print(merged.pop("b"))  # Output: 3
print(merged)  # Output: {'a': 1, 'c': 4}

popited_value = merged.pop("d", "Key not found")
print(popited_value)  # Output: "Key not found"
print(merged)  # Output: {'a': 1, 'c': 4

# Custom dict class that logs every key access and gets
class LoggingDict(dict):
    def __getitem__(self, key):
        print(f"Accessing key: {key}")
        return super().__getitem__(key)

    def get(self, key, default=None):
        print(f"Getting key: {key} (default: {default})")
        return super().get(key, default)

# Example usage
log_dict = LoggingDict({"a": 1, "b": 2})
print(log_dict["a"])        # Logs: Accessing key: a
print(log_dict.get("b"))    # Logs: Getting key: b (default: None)
print(log_dict.get("c", 0)) # Logs: Getting key: c (default: 0)

# OrderedDict: explicit insertion order tracking
from collections import OrderedDict

# Create an OrderedDict (insertion order is preserved)
od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print("Original insertion order:")
print(od)  # OrderedDict([('first', 1), ('second', 2), ('third', 3)])

# Move 'first' to the end
od.move_to_end("first")
print("After moving 'first' to the end:")
print(od)  # OrderedDict([('second', 2), ('third', 3), ('first', 1)])

# Move 'second' to the beginning (last=False)
od.move_to_end("second", last=False)
print("After moving 'second' to the beginning:")
print(od)  # OrderedDict([('second', 2), ('third', 3), ('first', 1)])

# Deep comparison of nested dictionaries
def deep_equal(dict1, dict2):
    """
    Recursively compare two dictionaries for deep equality.
    Handles nested dicts at any level.
    """
    # Base case: both must be dicts
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return dict1 == dict2
    
    # Check same number of keys
    if dict1.keys() != dict2.keys():
        return False
    
    # Recursively compare values
    for key in dict1:
        val1 = dict1[key]
        val2 = dict2[key]
        
        # If value is dict, recurse; otherwise, compare directly
        if isinstance(val1, dict) and isinstance(val2, dict):
            if not deep_equal(val1, val2):
                return False
        else:
            if val1 != val2:
                return False
    
    return True

# Test deep comparison
d1 = {"a": 1, "b": {"c": 2, "d": 3}}
d2 = {"a": 1, "b": {"c": 2, "d": 3}}
d3 = {"a": 1, "b": {"c": 2, "d": 4}}

print(f"d1 == d2: {deep_equal(d1, d2)}")  # True
print(f"d1 == d3: {deep_equal(d1, d3)}")  # False (d1['b']['d'] != d3['b']['d'])

# __missing__ hook: auto-vivification of nested dicts
class AutoDict(dict):
    """
    A dict subclass that automatically creates nested dicts on missing keys.
    Accessing a non-existent key returns a new empty AutoDict instead of raising KeyError.
    """
    def __missing__(self, key):
        # Create and insert a new AutoDict for missing keys
        self[key] = AutoDict()
        return self[key]

# Example: no need to pre-initialize nested structures!
config = AutoDict()
config["database"]["host"] = "localhost"
config["database"]["port"] = 5432
config["cache"]["redis"]["host"] = "127.0.0.1"

print("Auto-vivified nested dict:")
print(dict(config))  
# {'database': {'host': 'localhost', 'port': 5432}, 'cache': {'redis': {'host': '127.0.0.1'}}}

# Access and print
print(f"Database host: {config['database']['host']}")  # localhost
print(f"Redis host: {config['cache']['redis']['host']}")  # 127.0.0.1

# Dict with dataclass values
from dataclasses import dataclass

@dataclass
class Student:
    """A student object with id, name, age, and grade."""
    id: int
    name: str
    age: int
    grade: str

# Create a dict of students keyed by ID
students = {}
students[1] = Student(id=1, name="Alice", age=20, grade="A")
students[2] = Student(id=2, name="Bob", age=21, grade="B")
students[3] = Student(id=3, name="Charlie", age=19, grade="A+")

# Access and display
print("\nStudents database:")
for student_id, student in students.items():
    print(f"ID {student_id}: {student.name} (Age: {student.age}, Grade: {student.grade})")

# Get a specific student
alice = students[1]
print(f"\nFound student: {alice.name} with grade {alice.grade}")

# Update a student
students[2].grade = "A-"
print(f"Updated Bob's grade to: {students[2].grade}")



