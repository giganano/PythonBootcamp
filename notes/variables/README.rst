
Variables 
=========
Variables are objects that you've given a name. This allows you to store data 
in memory, and access it elsewhere in the code. 

Variables can have any name, and can be assigned to anything. However, it is a 
bad idea to give variables the same name as python built-in, because it will 
override the built-in function. For example, naming a variable ``print`` would 
cause the print function to disappear, because it now corresponds to a 
variable. 

Variables can be created with a simple declaratory statement with the equals 
sign. In all coding, ``=`` is not a mathematical statement, instead serving as 
the assignment operator. It tells the computer to store a value in memory and 
what to recognize it as. 

Consider the following example. 

.. code:: python 

	>>> x = 3 
	>>> print("The value of x is", x) 
	The value of x is 3

The output of this code is the simple string ``The value of x is 3``. 

Weak Typing 
-----------
Python is said to be a "weakly typed" langauge in that variables do not need 
to be assigned a ``type`` by the user. The python interpreter determines that 
automatically. 

To determine the ``type`` of a variable, use the ``type`` keyword. 

.. code:: python 

	>>> x = 3 
	>>> print(type(x)) 
	int 

The output of this is simply ``int``. This is the identifier for integer type 
data. Alternatively, 

.. code:: python 
	
	>>> x = 3.1 
	>>> print(type(x)) 
	float 

The output of this is ``float``, the type identifier for real numbers. 

.. code:: python 

	>>> x = "example" 
	>>> print(type(x)) 
	str 

``str`` is the type identifier for strings, which is printed here. 

Most coding languages are strongly typed, in that the user has to declare 
the type of their variables long with the variables themselves. For example, 
the following line in ``C`` would initialize an ``int`` with the value of 3. 

.. code:: C 

	int x = 3; 

Python developers do not need to worry about this, but should be aware of it 
if they decide to expand their skills to another language. 

Type Casting 
------------
Despite its automatic nature, user's retain the same power over their variable 
types as in other language through type casting. In this manner, integers 
and floats can be converted to one another, to strings, lists to tuples and 
vice versa, as well as other combinations of compatible data types. For 
example: 

.. code:: python 

	>>> x = 3 
	>>> x = str(x) 
	>>> print(type(x)) 
	str 



