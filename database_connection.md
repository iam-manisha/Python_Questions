DATABASE CONNECTION:
It is phenomenon of making the control to interact with database by being
these in python file
Using the process it is possible for backend developer to communicate
with database easily
Before communicating with database it is required to get accessibility
or need to establish a connection between python file with database file
To do the connection "connect()" function is used

    import sqlite3
    var - sqlite3.connect('database.db')

    To do the required operations in database following functions are used
    1.cursor():
    	It is function which is used to make the control to get pointed

to particular location in database
2.execute():
By using execute function it is possible to write and execute queries
of SQL
3.commit():
This function is used to save all the changes done for database

SYNTAX:
var1 = sqlite3.connect("demo.db")
var2 = var1.cursor()
var2.execute(query)
var1.commit()
