webit
===============
A web tools by Python.

Install
===============
::

 pip install webit


Use
===============
cd to you working directory and run command:

::

 webit.bat

if can't find webit command, try:
::

 python -m webit


open broswer with url **http://127.0.0.1:8000**, add shell script and run it.


Other tips
===============
1.set http port 80
::

 webit 80

2.authenticate with username and password (admin admin)
::

 webit -u admin -p admin

3.set the working directory (/tmp)
::

 webit -d /tmp

4.bind address with 127.0.0.1
::

 webit 127.0.0.1:8000
 
5.use as wsgi
::

 # set username and passwor
 export WSGI_PARAMS="-u admin -p admin" 
 # run wsgi with gunicorn
 gunicorn -b 0.0.0.0:8000 webit.wsgi:application

 