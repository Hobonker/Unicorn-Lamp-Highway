# Unicorn Lamp
Total Time ~ 20 hrs (31 hrs after revision)
# 5/24/25
I brainstormed what I wanted to do this day. I wanted to build something cool to put into my dorm and I decided to go for a lamp. I did research on what I wanted to use and then did my schematic. I've only ever used KiCad once before this so it took a bit.

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Schematic%20Lamp.png)

Time ~ 3 hrs

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
This is my third time using fusion if I just realized I couldn't do the thingy to two components I would've slept like 2 hours earlier ugh

Time ~ 6 hrs

# 5/29/25

I put the LEDs into the CAD and I realized that combining them is pointless because I have to split it in order to print anyway so I just added the LEDs in the seperate files and I also redid the hollow parts on them because I didn't use shell correctly previously.

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Hollow%20Head%20Unicorn.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/LED%20Circuits.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Hollow%20Torso1.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Hollow%20Torso2.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Hollow%20Head%20Connection.png)

Time ~ 5 hrs

# 8/3

So I'm back and I changed the wiring to a PCB 

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/KiCad%20PCB.png)

Then I CAD it, it was too big at first so I made it a bit smaller than the previous image

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Unilamp%20PCB.png)

I made full assembly with head, body and PCB, edit head to fit the PCB into hole, there's gap inbetween so you can see the hollow part of it still.

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Full%20Assembled.png)

Time ~ 5 hrs

# 8/5

I made assembly of head and whole lamp without any spaces

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Connected%20Full%20Assembly.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Connected%20Lamp%20Head.png)

Time ~ 1 hr

# 8/6

I technically started working 10pm ish on 8/5 but it's after 2 am right now on 8/6 so I'm just gonna journal here

Added in screw supports for my unicorn head to screw on, made the body backboard area flat, made the head connecting area flat, changed head hole from square to circle to fit same place on body, cut off some of the bottom of the head so it fits onto the body without any clipping. Uh I made like 4-5 different iterations shoutout Tanishq & Sharon for helping me and pointing out issues!

![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/FINAL%20Full%20Assembly.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/FINAL%20UniBody.png)
![image](https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/FINAL%20UniHead.png)

Time ~ 4 hrs

Yeah so I'm still here it's 4 am I uh changed the hole in the unicorn head to be smaller so the PCB would definitely not fall through, added CAD for battery pack and mount.

!image[https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/BatteryPack.png]
!image[https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/Lamp%20Head%20Smaller%20Hole.png]

Time ~ 1 hr (I spent like half the time waiting/recieving feedback so it's only 1 hr not 2 from 2-4 am)

Yeah its 5 AM, power bank go bye bye, wall cable go hello, remove all the work I just did for the battery and make new hole in body for wall cable. Head hole become even smaller.

!image[https://github.com/Hobonker/Unicorn-Lamp-Highway/blob/main/Images/PCB%20does%20not%20fall%20into%20this%20one.png]

I am ONE HUNDRED PERCENT SURE THIS PCB IS NOT FALLING INTO THIS HOLE WHY IS THIS THE 5000th time I've had to remake this hole. Update BOM and README with new changes.


