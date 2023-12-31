#PMDD Mood Tracker App
# The executive summary
This application is a mood tracker for women who suffer from PMDD. This application will help users track their moods and emotions so that they can better predict the outcome of the day and understand themselves better. In paticular, this app will ask what the users mood is, rate anger, sadness, loneliness, and happiness. This app will have a calendar that is color coded or setup in a way to show moods, anger levels, sadness levels, lonleiness levels, happiness levels, and period cycles at a glance. When clicking on a certain date in the calendar, this app will show the details of the mood on that date and any additional comments. This app will have a emotion selection with faces (hopefully) to display emotions while automatically setting the date for when the emotion was selected. Once the emotion was selected, a set of questions will be asked to rank emotions and a comment section. Based on the response, the calendar will be colored accordingly. User data will be tied to logins or user selector at the very beginning. People with PMDD suffer from extreme mood swing that can (usually) be predicted as long as proper tracking is in place and period cycles are considered "normal". This app will assist with that and help prepare and predict for any possible bad mood swing days to help the person and everyone around the person with PMDD. 

## Installation
'''bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser
'''
# High level installation from a container using docker and django. 

## Getting Started
To run my PMDD Mood Tracker App follow the instructions below
'''bash
docker-compose up
'''
#There will be in-app menus or help buttons for help with using specific features

## License
MIT License

Copyright (c) 2023 asimonson17

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Docs

## User Stories
<!-- 
Changed user stories to be more realistic. 
As a **parent**, I want to **be able to see my families calendar at a quick glance** so I can **prepare for the day**.
Acceptance Criteria - A share calendar option exists
As a **friend**, I want to **be able to see my friends shared notes** so I can **be there for them the day they're not feeling well**.
Acceptance Criteria - a share notes option exists
As a **woman**, I want to **be able to notate my moods in an easy way via pictures** so I can **documtent my moods quickly and efficiently**.
Acceptance Criteria - emojis exist in calendar to quickly notate moods
As a **user**, I want to **be able to see if I have PMDD with a quick test** so I can **get proper medical care**. -->
As a **user**, I want an **add entry feature** so I can **log my days** in a tracker.
Acceptance Criteria - An add entry button exists.
As a **user**, I want to be able to **see my notes at a quick glance** so that I **can see patterns**.
Acceptance Criteria - A notes view with cards exists on the tracker page
As a **user**, I want to be able to **create** an account so I can privately **track my information**. 
Acceptance Criteria - A registration button exists.
As a **woman**, I want to be able to **notate my moods in an easy way via pictures** so I can **document my moods quickly and efficiently**.
As a **user**, I want to be able to **see if I have PMDD with a quick test** so I can get **proper medial care**.
Acceptance Criteria - a test link exists to check for PMDD


## Mis-use Stories
As a **malicious user**, I want to **be able to see other users notes** so I can **use their informaiton in a malicious way**.
Mitigation criteria user login required to see data with least privilege enfored
As a **malicious user**, I want to **be able to insert false informaiton or alter users tracking** so I can **get them to click on a malicious link**.
Mitigation criteria Input validation required in all fields
As a **abuser**, I want to **be able to see peoples patterns** so I can **use it against them or gaslight them**.
Mitigation criteria Least privileged enfored. Cannot see others data without it being shared with you. Ability to revoke sharing.
As a **scammer**, I want to **be able to see peoples patterns** so I can **try to get them to buy a fake product for their specific PMDD symptoms**.
Mitigation criteria user login required to see data with least privilege enfored

## Diagrams - Markup

Here's our logo (hover to see the title text):

Homepage: 
![alt text](PMDD_Tracker/Images/HomePageSketch.jpg "Homepage")
Tracking Calendar:
![alt text](PMDD_Tracker/Images/TrackingCalendarSketch.jpg "Tracking Calendar")
Calendar Overview:
![alt text](PMDD_Tracker/Images/CalendarViewSketch.jpg "Calendar Overview")
Add Entry Page:
![alt text](PMDD_Tracker/Images/AddEntrySketch.jpg "Add Entry")
Login Page:
![alt text](PMDD_Tracker/Images/LoginPageSketch.jpg "Login Page")

C4 Diagrams:
![alt text](PMDD_Tracker/Images/Project_1_milestone_C4_Chart.png "C4 Diagram")


## Notes
The templates where my coding is mainly is in here: PMDD_Tracker\PMDD_Project\templates - I did the html, css, and js files but haven't tied them to django yet.
