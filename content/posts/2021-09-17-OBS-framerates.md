---
author: Stephen Adams
date: 2021-09-17 08:34:28+00:00
draft: false
title: OBS Framerates
type: post
url: /2021/09/17/OBS-framerates/
image: /img/streaming-pc.jpg
#tags:
#LIST: books,code,comics,everything,fatherhood,gadgets,games,internet,life,movies,music,nerd,podcasting,politics,random,science,tech,tv,video,work,writing
tags:
- tech
- games
- internet
---

If there's anything that might be worth getting right when it comes to streaming your video games, it's presentation. Having a camera is nice. Having a good microphone so people can hear and understand you is even better. But, we're talking about streaming video games and one of the things you want to look the best is the game. I ran into an issue recently where, despite having a super beefy machine, I was unable to get my framerate smooth for the viewers. The images themselves looked pretty good, but overall it was just "chugging" a bit.

I ended up down a rabbit hole, trying to figure out why everything seemed just a bit laggy. It brought me to a few realizations.

First, my camera was set to 1080p. That might sound like a pretty innocent setting, all things considered. I have a camera that's capable of 1080p/30fps so I might as well use it right? Well, it turns out that even after a few decades of webcams being a thing, processing incoming video is still a pretty huge CPU hog. To be honest, I didn't even remember setting my camera to 1080p, and there really is no practical reason that it should be that high. I can't imagine a single scenario where a person might full screen my big dumb head on their television or monitor. Mostly, I'm going to be in a small square on the screen, and even if I am in a one on one conversation via some chat app, I'm going to be in a square next to the person I'm talking to. There's really no reason for 1080p. 

I ended up setting it to 720p and that immediatley cleared up camera smoothness issues. My camera was smooth, but my game was still a bit jaggy. Time to dig a little deeper.

The next thing I decided to try was just reducing the in game settings. I was playing a **fantastic** game called [The Outer Worlds](https://outerworlds.obsidian.net/en/enter)  which is a few years old now, so it's not as difficult to run as some newer games might be. I had it set to Ultra graphics, 144 FPS, and 1440p resolution. I have a graphics card that can do all this and a monitor that can support, so, much like the webcam, why not? Well, I figured it was worth a shot dialing things down a little bit. I took a note out of my friend [Bill's](https://www.youtube.com/NerdNest) book, and decided that "resolution doesn't matter" and dialed it down to 1080p. Honestly, I expected more of a difference in fidelity, but I actually think Bill is right. I still had all the ultra settings turned on, but now that the resolution was reduced, I wasn't able to tell that much difference and the stream seemed to smooth out considerably.

Now I had a new problem. Playing in fullscreen at 1080p, when my desktop is set to 1440p, caused some really annoying resolution changes any time I had to do an alt+tab to switch to my chat or adjust something in [OBS Studio](https://obsproject.com/). My screen would go black for a couple seconds while everything rearranged itself to fit the new resolution. This was super inconvenient, and quite honestly, I'm just not one to tolerate these kids of situations. Deeper down the rabbit hole I went!

I ended up finding a handful of pretty decent guides on optimal OBS settings and followed them. They didn't fix the problem I was having, but I was introduced to the [optimal nVidia OBS settings](https://www.nvidia.com/en-us/geforce/guides/broadcasting-guide/) that they partnered up for. I was running at a lower bitrate to twitch than I needed to, and I could change a couple other things that were actually pretty helpful overall to my stream. Still no fix for the frame issue though.

Then, **I found it**.

I have a 144hz monitor, which is great! Especially when my graphics card can pump out that many frames a second during a fast paced game. But it turns out that this speed just doesn't jive with OBS. OBS has a framerate range of 30 - 60FPS that it can push. I'm not entirely sure how all the underlying mechanisms work with it, but if I set my game back down to 60, everything streams super smooth. The weird thing, and the most frustrating, is that the game itself when maxed at 144, is just fine. The game isn't having any issues on my screen, but the stream is just not working with it. I wonder if it's related to key frames, or a capture bottleneck in the software somewhere. I really just don't know. What I do know is that bumping the framerate down fixed it. Even though it's not quite as smooth as it was, it's barely noticeable. Which has gotten me to start questioning any review of any monitor touting its refresh rate. I'm not a competitive shooter kind of gamer, so I don't know that it should really matter to me. I mean, I can tell a difference between 60 and 144, but how much difference? Not much.

Bonus content! In other news, I did learn a trick related to OBS that you might find handy. If you have any game captures setup in your scene that you're using to play your game. They are ALL doing work at the same time. The game capture source is meant to poll for the game its supposed to watch about every 5 seconds or so. This apparently can eat some resources and often cause frame dips while your playing. The solution is to hide all the game captures that you aren't using. If you can swing it, just delete them entirely and update the single game capture to grab a different game. I know everyone has different workflows here, but you might as well give it a go. 

I hope you learned something from this! I know I did.

tl;dr

* Set your webcam to 720p. Webcams are expensive
* Set your game to 60 FPS. OBS can't send more than that anyway
* Hide all the game captures that you aren't using 
* If necessary, reduce your resolution. Keep ultra/super/high settings, but dropping resolution can help a lot.
