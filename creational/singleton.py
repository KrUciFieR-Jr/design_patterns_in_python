"""
Singleton pattern is responsible for creating only one instance of a class.
Useful when one action needs to be coordinated throughout systems.
Applicability:

- When there should be only one instance of a class, and it must be accessible to all clients from a well known access point
- Extensible using subclassing, and cleints should be able to use an extended instance

Structure:
    - Private constructor - prevent instantiating new objects
    - Static method or property - global point of access
    - static varible - holds the instance of the class

Benefits:
- Creates one object and reduces repeated object creation saving resources
- Controlled Access

Drawbacks:
- Global state - if not managed carefully can lead to unexpected side effects
- Diffuclty in testing, since the instance state is carried onto different tests

cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

basically you can do super(cls) -> but when user extends this class
there is a possiblity that MRO can fail so make the resolution clear


we say super(Base class, instance of class).__new__(cls)
                                                |
                                                |
                                            instantiate a new object
Check extras.txt

method of the base object class to create a new instance of Singleton.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance._initialize(*args, **kwargs)  # Initialize only once
        return cls._instance

    def _initialize(self, *args, **kwargs):
        # Initialize the singleton with the provided value
        self.value = kwargs.get("value", None)


# Usage
s1 = Singleton(value="First")
s2 = Singleton(value="Second")

print(s1.value)  # Output: First
print(s2.value)  # Output: First
print(s1 is s2)  # Output: True


import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                cls._instance = super(Singleton, cls).__new__(cls)
                cls._instance._initialize(*args, **kwargs)  # Initialize only once
        return cls._instance

    def _initialize(self, *args, **kwargs):
        # Initialize the singleton with the provided value
        self.value = kwargs.get("value", None)


"""
Real time usage for this is :
Database, App configs, maintaining same logger for the app
"""

"""
import sqlite3

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('app.db')
            print("Database connection established")
        return cls._instance

    def query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

# Usage
db = Database()
result = db.query("SELECT * FROM users")
print(result)

"""