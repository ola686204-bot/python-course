**DATA STRUCTURE**
Choice
use seperate function for each calculator operation.
Reason
seperate functions make each operation easy to understand, test, reuse, and maintain.

Rejected Alternative
A single function containing all three calculations was rejected because it would give the function multiple responsibilities.




**Project Structure**
Choice
Store calculator and greeting functionality inside the 'modules' directory.
Reason
seperating reusable functionality from entry-point files keeps the project organized and makes the modules easier to reuse.

Rejected Alternative
Putting all code inside 'main_greeting.py' was rejected because it would mix the user interface with reusable functionality.