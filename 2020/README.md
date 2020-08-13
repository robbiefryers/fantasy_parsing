# Draftfantastyfootball Stats Dashboard

Web scraper for getting data from draftfantasyfootball

---

## Steps


1. Run ``1_fetchHeadToHead.sh`` to generate and run curl commands that will output all of the match data to ``headtoHead.json`` 
2. Run ``2_pullMatchIDs.py`` to print out a list of all match IDs which we need to copy and paste into the Automator script
3. Copy the output from  the``2_pullMatchIDs.py`` script abd paste into the Automator script variable matchIDS, run the ``3_pullHTML`` script
4. Rub the``4_parseHTML.py`` script that will extract the points data from the html files and dump all the data to ``final.json`` 

fetch head-tohead JSON data. This writes the h2h data to h2h_data.json (including HeadToHeadMatche ID)
2. Regex pattern search ```"HeadToHeadMatch","_id":"[\w]{17,17}``` in ``h2h_data.json`` to get parse out h2h IDs
3. Immediatley after the destination pin is marked, the interpolated points should be calculated and plotted
4. The distance between the depart and destination should be calculated and displayed in the relevant input field
5. The number of interpolated points should also displayed in the relevant input field
6. Any further clicks should result in an alert to say the calculation has been completed and to reset the map
7. Hitting the 'Clear Map' button should reset everything and allow the user to plot another 2 markers
=

---

## Getting Started

This repository can be used as a template and includes a Google Maps API key, so you will not need to configure anything.

1. Create a bare clone of this reposistory to your local machine using the command in step 2
2. ``` git clone --bare https://bitbucket.org/robbiefryers/waytob_test.git```
3. Modify the template and implement the above logic using javascript.
4. Mirror push the changes to a **new** repository on your personal online github/bitbucket/other using the command in step 5
5. ```git push --mirror https://bitbucket.org/your_account_name/waytob_test.git```

---


## Submitting your solution

Send a link to your mirrored repo to robbie@waytoB.com so I can clone and check it