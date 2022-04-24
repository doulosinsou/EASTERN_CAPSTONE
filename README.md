# EASTERN_CAPSTONE
Lucas E Moyer

This project is in fulfillment for Eastern University's DTSC691, the Applied Captstone for MS in Data Science, term Spring2 2022. Lucas E Moyer is submitting this website and all it's underlying code and database to satisfy the requirements for the Database track, approved by Dr. Gregory Longo. 

## Project Goals
Fundamentally, my purpose is to create a functional website using a database for all content. The website hosts multiple blogs (called topics) by multiple authors and contributors. Viewers can access public topics, subscription topics, and private topics based on their level of authentication. The site will display sufficient pages and links to navigate content and authors, including available topics, tags, and posts.

Viewers will be able to simulate roles and logins through a dropdown at the top of the site. By selecting their role, they see what one may see under a similar logged-in experience.

In addition, there is a dashboard for administrators to see visualized stats from visits, revenue, and subscribers. The public viewers of this project app will not be able to view these dashboards unless they switch to administrator. 

I also feature a simplistic search page, to find content in the blogs and display links.

This project is inspired by my previous work in web development and web hosting. I have desired for many years now to create my own template-style service for my clients. Such a project as this can easily be converted into my actual website creation workflow. I will not create the UX for user management for this project. I will focus instead on Database creation, access, and functional server delivery. 

At the time of submission, the server must be locally hosted, although the database is successfully hosted through my own shared servers. The video walkthrough will show the functional features of the website while running on my machine. When uploading projects of this sort, there are too many bugs related to server requirements and malware protection for me to make part of this submission. However, once sufficient bugs are worked out, it will be made public as a portfolio through my personal website.

## Project Limitations
Although the final application of the project will be as a personal portfolio and potential website hosting platform for my personal business, this submission is not hosted on the internet. The server is locally hosted with Flask. The Database itself is hosted on my servers. Permissions for access will be displayed at the appropriate location in the coding process below. This access is only intended for the reviewers of this project as required for the Capstone evaluation. Production of this project would hide these parameters (it is currently hidden from my .git files). 

The project can be fully replicated by following the instructions at the end of this document called “Building the Project” 

Further, this ‘portfolio-like’ project does not intend to handle:
- security logins 
- search sanitizing
- automatic emails
- financial transactions
- subscription collections
- statistics gathering

A basis for these is prepared for, and the format for use is existent. 

## Building the Project
Here is a bullet point walk through for rebuilding the project. This assumes that you have access to the .zip files and either a local or web MySQL server with personal access credentials. 

Boot up an SQL server
- Connect with Workbench 
- Load .sql files from the sql_files folder on root
- Create a custom database (mine was “moyeraud_website-builder”) 
- Build the tables and basic inserts from `capstone_init` and `INSERTS` and `ViewsFuncProc` (be mindful of known INSERT bugs based on Primary Keys with timestamps)
- Use the rest of the files as references for queries
- Supply the login information to mysql.connector at the top of `customSQL.py`
- From terminal, run `generate_posts.py`, `generate_stats.py` and `generate_revenue.py` in that order
- Run Flask using `webapp.py` as the entry file

