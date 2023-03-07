# AIRBNB CLONE PROJECT 
# Description
This is a team project to build an [AiRBnB clone console.](https://www.airbnb.com/)
The console handles object storage using JSON serialization and deserealization. This is a team project to develop a Python3 console that emulates the AirBnb object management. It includes directory with static web pages for desktop and mobile first version with ARIA implementation.
## The first step
The first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration
Each task is linked and will help to:

* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Testing
All the tests are defined in the test folder

All your tests should be executed by using this command:
### Modules
```
python3 -c 'print(__import__("my_module").__doc__)'
```

### Functions (inside and oytside the classes)
```
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

### Classes
```
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```
All tests should also pass in non-interactive mode: 
```
echo "python3 -m unittest discover tests" | bash
```

## Authors
- Nnenna Udefi
- Oluwaseun Olorunshola
