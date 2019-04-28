# CanIt!
CanIt! is an application designed to help individuals and groups keep their communities clean.

## Main Features
(Aspects of these features planned but not implemented are in italics)

### User Accounts
Users can create accounts. Required fields are first name, last name, a username, an email, and a password (with confirmation). Users can alter these details, except for password. 
*Email verification will be required. Password changes will be allowed on a separate page, and users will be required to input their current password." 
*Users should be able to decide to whether their username or real name is attached to their actions*

### Spot Marking
The app uses Google Maps API to allow users to mark littered areas with pins. These pins are then stored in the database with their latitude and longitude.
A separate page displays the map with all user pins across the world. 
*Users should be able to set default options like the distance to show. The map should center on their location as long as location is enabled. Filters will be added so users can filter out recently cleaned spots, spots that have low verification ratings, or spots below/above certain levels of pollution. When a user marks a spot they should be required to add a level of pollution (low/moderate/severe)*

### Event Creation
The app allows users to create events tied to a location on the map. These could be locations they added themselves, or locations marked by others.
*Users should be able to join and leave events created by others. Users should be able to request a route from their default location or current location to the spot, which would utilize the Google Maps Routes API.*

## Future Plans
**Future plans are listed in order of priority**
- Users should be able to upload photos tied to events (before/after) or spots (reference) directly.
- Social media integration:
	- Twitter - connect for account creation and login, display running "#trashtag" tweetboard, allow posting of uploaded photos, and eventually give users the option of sending out pre-composed tweets of before/after pictures or a newly marked spots.
	- Facebook - same as Twitter, but additionally allow events to be posted to Facebook so users on Facebook can join them as well, augmenting the networking power of the app.
	- Instagram, mostly for sharing the photos
- Gameification to encourage users to participate. Points for marking spots, cleaning spots, etc, to encourage participation. Will need some careful planning and verification systems to avoid potential exploitation

## Technologies
- Written in Python 3.6
- Uses the Django 2.2 framework
- Makes use of Google Maps API
- Uses the jQuery library for JavaScript
- Uses SASS for styling, using the [script created by Prescott Breeden](https://github.com/prescottbreeden/SASS-create-project-script)
