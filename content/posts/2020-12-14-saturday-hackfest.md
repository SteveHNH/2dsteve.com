---
author: 2dsteve_ty3fxq
date: 2020-12-14 23:16:09+00:00
draft: false
title: Saturday Hackfest
type: post
url: /2020/12/14/saturday-hackfest/
---




It’s probably obvious to most people who follow any of the [content I make](HTTPS://www.legion of dorks.com), that I’ve been spending most weekends at home doing projects and otherwise NOT GOING FLIPPIN’ ANYWHERE for most of 2020. I’m not bitter about it, I swear. Anyway, this last weekend I went on a really inconsequential journey. One that most people might not give a flip about. I’m about to get super nerdy, so if you don’t care, just turn back while you can. Otherwise, strap yourself in and grab a cup of Mountain Dew.







On Friday of last week, I got the wild idea that I should try to build a streaming box. In other words, I should just game on my gaming PC and send all of the “bits” that make up a stream over to another machine that actually can do all the encoding and streaming. This used to be super common before on-GPU encoding chips came along, and I wondered if I would benefit from in.







The inception of this idea came from the charity stream. I experience some pretty insane frame drops when playing Red Dead Redemption 2 with Jacob. It really bummed me out because I was sure that I had done it before without much issue. I just got curious about what a stream box would look like.







Let’s solve problems! I already had a capture card for capturing console stuff like my PS4 and switch, and Sam had my hand me down PC. He wasn’t using it, so my hardware needs were pretty much handled. On to the real stuff! 







## **Audio**







The first thing was trying to figure out how I would get audio over to the stream box. I still wanted to use my microphone on my main machine because I videoconference with it. I also had no need to podcast off a stream machine. That kind of streaming wasn’t the least bit resource intensive, so I needed all my main hardware to stay connected to my gaming rig. But HOW was I going to get the audio over to the other machine. Enter my buddy, Zaepho, and the suggestion of VBAN!







VBAN is an audio streaming tech built into a software mixing application called [Voicemeeter](https://vb-audio.com/Voicemeeter/). Voicemeeter has become a major part of my content creation workflow because I can route and control audio on my PC without needing a hardware mixer to do it. It’s a very powerful piece of software and FREE. VBAN is a way to send any of the channels in Voicemeeter to a remote voicemeeter or VBAN receiver of any type.







I had a blast playing with VBAN. It couldn’t be easier. Once it’s setup, you just configure the IP of the receiving machine on the host, and tell it what “bus” to send. You can do your main output, or breakout each channel into a separate “stream”. On the receiving machine, you indicate what IP you expect to get audio from and then tell it what destination “bus” to send it to.  Basically, think of it like a cable being plugged into an output and into an input, but that cable is your home network and you can change where it goes on the fly.







## Video







Once I got that wired up and working, I needed to figure out how to get the video signal from my machine over to the other one. I could capture it when playing a game, but I wanted to use my webcam on my main rig. I didn’t want to have to move it to the other machine, and I definitely didnt’ want to have two of them. That’s when I thought about NDI.







[NDI](https://ndi.tv/tools/) is a technology for sending video signals over the network. Luckily, my software of choice, [OBS Studio](https://obsproject.com/), has a plugin to support this thing. So all I had to do was install the OBS plugin and it’s requirements, then tell OBS to output the main window as an NDI signal. It automatically starts up and allows NDI receivers to connect to it. I created a “scene” in OBS and made my webcam the only item in that scene. So I had a big ol’ 1080p signal from my webcam to send across via NDI. 







On the remote machine, I installed the same OBS plugin, then added an NDI source. My signal from the host machine was already available, so I just chose it from the drop down and BOOM. I had a webcam signal from my gaming rig on the remote rig that I could resize and manipulate with ease.







## Capture







This was easy peasy. I already had the capture card, so all it took was running an HDMI out from my PC to the capture card, then an HDMI cable from the “output” on the capture card to my monitor.







It was easy, but it also is where my plan started to fall apart. I have two 1440p 155hz gaming monitors. I love these monitors because everything is so sharp. The bummer with the pass through is that the capture card could only send a 1080p signal. This would be great, but it makes everything SUPER fuzzy on a 1440p panel. On top of that, you can’t mirror a high res signal to a low res interface without it adjusting the high res to the lower resolution. I tried everything I could, but it just wouldn’t work that way. 







On top of that, I only have two monitors. So if I wanted to have the high resolution stuff for when I work, write, or do literally anything other than game, I needed to have the HDMI on a separate input. That meant that I had to hit physcial buttons on my monitor and switch inputs when I wanted to make sure my game was going through the capture card and I wanted to see it at the same time. That’s stupid.







The fix for THAT particular problem is a hardware cost. There ARE capture cards that allow for you to pass through up to 4K 60fps content. That would have done the trick, but I”m not spending money on that. That’s crazy pants. This is meant to be just a fun project for me. 







So I put that away. In the process though, I learned one more thing.







## Remote Desktop







Through all of this, the whole thing hinged on me being able to use the remote PC ... remotely. That also meant that I didn’t want to have a monitor hooked up to it. This is generally referred to as a “headless” system. It’s popular with servers because no one really needs to *see* it. They just need to be able to use it when necessary. The thing I discovered was that as soon as I unplugged the monitor, my remote software stopped working.







I tried using [TightVNC](https://www.tightvnc.com/). VNC is a very popular cross platform Remote Desktop protocol that allows you to see your machine from another machine. I had to go this route because for some reason Microsoft decided that Windows 10 Home users don’t need Remote Desktop. They’re wrong.







With that, I made the discovery that I couldn’t connect when the monitor was disconnected. I found a couple sites with supposed workarounds but none of them worked for me, and the overwhelming majority of websites suggested there was no solution to this problem. It’s possible it’s because of my Windows Home edition but I have not gone that far into it yet. 







I even tried a piece of software called Anydesk that was recommended by my friend, TVsTravis, that was also supposed to do the trick. It didn’t work for me, but I’m keeping it around because I really dig the interface for it. It’s nifty and free for private use.







The solution come down to a tiny dongle that you plug into your HDMI, DVI, DisplayPort, or VGA (depending on the dongle you purchase) that tricks your system into thinking it has a monitor attached. This dummy dongle keeps the underlying windows display systems alive so you can connect remotely.







To be honest, that last part was seriously frustrating, but it was also pretty fun! I learned a lot from it.







## The Resolution







After all of that nearly day long hacking, I came to a resolution.







I’m just going to use the one box.







The main reason for this is that it turned out that my fix was a simple change within OBS Studio that completely resolved my frame rate problem. Turns out that OBS was so confident in my hardware that it automatically set the capture frame rate to 60fps. That seems awesome. Who wouldn’t want buttery smooth 60fps content to watch. The problem was that with high end games, even using the NVENC (hardware) encoder, it was too much for my GPU to handle and it was choking trying to process the extra frames.







I dropped that little value down to 30 and voila! It worked like a charm. No more stuttering and a less than noticeable difference in the actual streaming content. Now it ran at a satisfying yet not optional 30fps and looked good enough that it doesn’t bother me at all.







You may ask, but you didn’t end up with a box and you did all that work to try to dual-PC stream. You’re not wrong, but I gained a lot from the experience. Not every wild hare you have ends up with a successful project, or even attaining the goal you set out to accomplish. But it can teach you things you didn’t know before. Not only that, I had an absolute blast. I haven’t spent that kind of time just hacking on a personal project in ages. It was wonderful exercise and was really relaxing despite all the ups and downs of the project. 







If you made it this far, pat yourself on the back. That was quite the slog in the age of immediate gratification and Buzzfeed. This was fun. See you next time.



