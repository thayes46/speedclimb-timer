# speedclimb-timer
Open source timer for speed climbing

Not intended for professional use, initial use case is for kids' birthday parties to allow for kids to race

## How to operate

clone this repo and set it as a cron job to run the main script on boot

Once on, it will pull from a url given in speedtimer.py for what to display when not in use along the records

To enable, plug in both foot pedals and step on both for 1 second. 
The display will then show the timer for the orange and grey lanes instead of the url.

At this point a timer for a lane will be primed when the pedal is depressed, and will start as soon as it is let go.
The timer stops when the button at the top of the lane is pressed.

Once both lanes have been run, the lane with the shortest time will light up at the button at the top of the lane

If only one lane is being used, no lights will be used

If someone ever wants to add their time to the leaderboard, there will be a google form to add their name and time into