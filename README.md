# rent_seek

## Overview
For persons with rental properties looking to see active market listings. The goal of this project is to show trends and track data back to the inception of this program into the future. The project will be built in Django/

## Features
#### As a **rental owner** I want a simple way to see **active market statistics ex avg/low/high rental listings**.
### Tasks:
* Use scrappy to create a website scrapper. May use text or image recognition.
* Create a form for the user to fill out for the zip code, search radius, and 1 or 2 bedroom selection.
* Create a view that returns results for that zip code and previous history.
* Create a template to graph results.

#### As an **admin** I want to be able to vet users before they are allowed to use the program, reduce scrapper spam which could result in an ip address ban.
### Tasks:
* Create an admin
* Catch account requests and authorize them on a per person basis.
* Create a view for removing data.

### Additional Features:
* FAQ on how to use program or report erros.

## Schema (Data Model)
* UserSearch
  - user (foreign key to User)
  - zipcode (integer field, only 5 numbers)
  - bedrooms (integer field, only 1 or 2 rooms)
  

## Schedule
### Week 1
* Create & Clone Repo
* Create Virtual Environment
* Start Django Project
* Write Models
* Set up Scrappy
  
### Week 2
* More work on Scrappy, probably.
* Finish with Scrappy

### Week 3
* CSS
* Get search history working
* JS Graphs and or Charts
  
### Week 4
* deploy to heroku
* additional styling tweaks


## Feature Tiers:
### Must Haves
* Be able to pull market data from craigslist
* Individual accounts with history

### Should Haves
* Various graphics to represent accurate pricing.

### Can Haves
* Possibly pull data from other sources.
* Forum for discussions.
* 3 or 4 bedroom data.

### Won't Haves
* Payment system
