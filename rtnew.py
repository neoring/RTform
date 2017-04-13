#!/Users/astokes/anaconda/bin/python

import input_switcher
from os import environ
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import rt

# Define username and password from environment for API login
user_login = environ['RT_USER_LOGIN']
user_pass = environ['RT_USER_PW']

# Define Yes responses
yes = ["Yes", "yes", "Y", "y", "OK", "ok"]

# Define Subject & Body

subject_int = input('Enter subject: ')
body_int = input('Enter body text (brief description of issue): ')
requestor_int = input('Enter the requestor (username): ')
ticket_requestor = "".join((requestor_int,'@trinity.unimelb.edu.au'))

# User input
print('1 - Alex\n2 - Khuong\n3 - Stan\n4 - Ratna\n5 - Phuong\n6 - Noorallah\n\
7 - Wisam\n8 - Geoff\n9 - Hermann\n10 - Trent\n11 - Matt\n12 - Martin')

user_int = input('Enter user value: ')

ticket_user = input_switcher.user_owner(user_int)

# Cause input
print('1 - Client Side\n2 - Infrastructure\n3 - Systems\n4 - User')

cause_int = input('Enter cause value: ')

ticket_cause = input_switcher.user_cause(cause_int)

# Department input

print('1 - Advancement\n2 - Buildings & Grounds\n3 - Careers Office\n4 - Catering & Hospitality\n\
5 - Chaplaincy\n6 - College Wide\n7 - Conference/Visitors\n8 - Finance & Administration\n\
9 - External\n10 - Finance & Administration\n11 - FS Admin\n12 - FS Students\n\
13 - FS Teaching\n14 - I.T.\n15 - Library\n16 - Non Res Tutors/Students\n\
17 - Res Coll Staff\n18 - Res Coll Students/Tutors\n19 - Summer School\n\
20 - Theology Staff\n21 - Theology Students\n22 - Wardens Office')

department_int = input('Enter department value: ')

ticket_department = input_switcher.user_department(department_int)

# Location input

print('1 - 200V\n2 - Main Campus\n3 - Royal Parade\n4 - Swanston St\n\
5 - LSN\n6 - Bouverie St\n7 - EHH\n8 - Gateway\n9 - Other\n\
10 - NA')

location_int = input('Enter location value: ')

ticket_location = input_switcher.user_location(location_int)

# Impact input

print('1 - Critical\n2 - Significant\n3 - Limited\n4 - Minimal')

impact_int = input('Enter impact value: ')

ticket_impact = input_switcher.user_impact(impact_int)

# Urgency input

print('1 - Urgent\n2 - Priority\n3 - Minimal')

urgency_int = input('Enter urgency value: ')

ticket_urgency = input_switcher.user_urgency(urgency_int)

# Team input

print('1 - CS\n2 - Infra\n3 - EA')

team_int = input('Enter team value: ')

ticket_team = input_switcher.user_team(team_int)

# Category input

print('1 - AV - Faults including Echo 360\n2 - AV - Set ups or Standby\n\
3 - CITRIX Applications\n4 - Client Training Needs\n5 - Copyright\n\
6 - Desktop Computing\n7 - Email\n8 - File Services - Staff\n9 - File Services - Students\n\
10 - Internet - Eduroam/Wired Networks\n11 - iPad Hardware & Software\n\
12 - IT Account - Open & Close\n13 - IT Account - Password Reset\n\
14 - IT Orientation and Set up\n15 - ITS Housekeeping\n16 - Laptop Computing\n\
17 - Portal\n18 - Printing - Staff\n19 - Printing - Students\n\
20 - Projects (Client Managed)\n21 - Projects (ITS Managed)\n\
22 - Software Services\n23 - Student & Staff Cards\n24 - Synergetic - Faults\n\
25 - Synergetic - User\n26 - Synergetic-sql query\n\
27 - TCOLE including TurnItIn etc\n28 - Telephones - fixed\n29 - Telephones - Mobile\n\
30 - User Error / Training Need\n31 - Walk-in')

category_int = input('Enter category value: ')

ticket_category = input_switcher.user_category(category_int)

# Output user inputs for confirmation
print('\nCreating new ticket with Subject: {}'.format(subject_int))
print('and body text: {}'.format(body_int))
print('for requestor: {}'.format(ticket_requestor))
print('\nAssigning to user {}'.format(ticket_user))
print('Cause: {}'.format(ticket_cause))
print('Department: {}'.format(ticket_department))
print('Location: {}'.format(ticket_location))
print('Impact: {}'.format(ticket_impact))
print('Urgency: {}'.format(ticket_urgency))
print('Team: {}'.format(ticket_team))
print('Category: {}'.format(ticket_category))

confirm_int = input('\nPlease confirm the information is correct to create a new ticket (Y/N):' )

if confirm_int in yes:
	print('Logging in to Trinity RT...')
	# Log in to the Trinity College Request Tracker site
	tracker = rt.Rt('https://rt.trinity.edu.au/REST/1.0/', user_login, user_pass)
	tracker.login()
	print('Done.\nCreating new ticket...')
	# Create new ticket with detapils passed through
	tracker.create_ticket(id='ticket/new',\
	Queue='it_help',\
	Requestor=ticket_requestor,\
	Subject=subject_int,\
	Text=body_int,\
	Owner=ticket_user,\
	Status='Open',\
	InitialPriority=10,\
	CF_Cause=ticket_cause,\
	CF_Department=ticket_department,\
	CF_Location=ticket_location,\
	CF_BAU='BAU',\
	CF_Impact=ticket_impact,\
	CF_Urgency=ticket_urgency,\
	CF_Team=ticket_team,\
	CF_Category=ticket_category
	)
	print('Done! Exiting.')
else:
	print('Ticket information not confirmed. Exiting.')









