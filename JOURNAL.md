# Unicorn Lamp

# Inspiration
I'm going to a boarding school so I need stuff for my dorm there. The mascot of the school is unicorns so I decided to try my best shot at a unicorn lamp since I needed a lamp.

# 5/24/25
I brainstormed what I wanted to do this day. I wanted to build something cool to put into my dorm and I decided to go for a lamp since I had some lights and microcontrollers left over from an old project I did before highway so it was a good way to repurpose it. I went through my old stuff to make sure it would work for this project and then did some research online about lamps and tinkered with my LEDs and Arduino.

Time ~ 2 hrs

# 5/26/25
Realizing I need to lock in I started modeling the base

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Torso%20Bottom.png)

I uh tried to do sweeping but miserably failed so I just decided to do like 10 circles spaced from each other and lofted them. I tried to space the circles so they would form an arch on the back and come in from the front since that's what a horse/unicorn head looks like. I really should've just done a cylinder shouldn't I.

Time ~ 3 hrs

# 5/27/25
So yeah uh 20 circles, offset planes, and lofts later (more like 50 with the amount of times I redid them why is it so hard to make an arching back using spaced lofts holy)

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Lamp%20Torso.png)

I cut off some of the top part of the torso since I want to nest the head in there. Doing the head tomorrow (I've been making circles for hours now I need sleep)

Time ~ 3 hrs

# 5/28/25 
Yay the head is actually kind of nice for my poor drawing skills

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Lamp%20Head.png)

Also why is there LITERALLY no like skribble line in fusion this is absurd your telling me I can't just draw it and I have to make like 20 arcs? (theres probably a feature somewhere I couldn't find)

Ok so I'm realizing if I just put the head straight onto the torso its gonna be a super abrupt change so I'm gonna try to fillet everything. After I assemble the components into one file.

So it turns out I actually can't fillet two different components because they're unlinked and if I unlink them and then try to combine them it makes like a copy of the combined portion but then there's like this thingy it leaves behind like it makes two torsos and one of them has a head but if I delete the torso without the head the rest of it goes kaplooey because the one with the head is refrencing the one without one so uh yeah.

I just ended up exporting the DXF file for the head sketch and aliging it in the torso drawing then re extruding it back to life so it's just one component now but I still have the seperate components so I can print them seperately. Then I fillet everything and i also revolved some features to connect them to the head. I'm probably gonna need to sandpaper a lot of this down to make it smoother.

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/unicornlampbody.png)

Working in fusion at 2 AM is not it

Time ~ 6 hrs

# 5/29/25

Repository I summon you and I also polished some of the cad. I'm gonna use the light as a horn hence the lack of horn in the cad. It'll hopefully look like a laser shooting out of it's head once I build it.

Time ~ 1 hr
