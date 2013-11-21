PennSchedule
=========

PennApps Fall 2013

Team
----
Adel Qalieh -- Front End -- @adelq  
Prakhar Bhandari -- Python Backend -- @pbjr23  
David Lakata -- Flask -- @dlakata  

Technology Colophon
-------------------
HTML5, CSS3  
Bootstrap  
Normalize.css, jQuery, Modernizr, FullCalendar.js  
Python, Flask  

Getting Started
---------------
1. Install virtualenv on your computer
2. Create a virtualenv for PennScheduler
```shell
$ virtualenv pennscheduler
```
3. Activate virtualenv
```shell
$ cd pennscheduler
$ source bin/activate
```
6. Install Python module dependencies, namely `Flask` and `icalendar`
```shell
$ pip install flask icalendar
```
5. Clone git repository into directory
```python
$ git clone https://github.com/dlakata/PennScheduler.git
```
6. Start server
```shell
$ python PennScheduler/app.py
```
