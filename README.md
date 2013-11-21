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
1. Install [virtualenv](http://www.virtualenv.org/) on your computer
2. Create a virtualenv for PennScheduler

```
$ virtualenv pennscheduler
```
3. Activate virtualenv

```
$ cd pennscheduler
$ source bin/activate
```
4. Install Python module dependencies, namely `Flask` and `icalendar`

```
$ pip install flask icalendar
```
5. Clone git repository into directory

```
$ git clone https://github.com/dlakata/PennScheduler.git
```
6. Start server

```
$ python PennScheduler/app.py
```
