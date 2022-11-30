---
author: Stephen Adams
date: 2021-01-26 21:57:51+00:00
draft: false
title: The Podman Quest
type: post
url: /2021/01/26/the-podman-quest/
#image: /img/some_featured_image.jpg
#tags:
#LIST: books,code,comics,everything,fatherhood,gadgets,games,internet,life,movies,music,nerd,podcasting,politics,random,science,tech,tv,video,work,writing
tags:
  - Nerd
---

Okay, ya'll. I have been watching a LOT of programming streams on Twitch and there is one theme that seems to be pretty constant between all of them: [Docker](https://www.docker.io) is the thing. I hear Docker almost constantly when they are talking about containers, and I'm bothered by it. It's not that Docker isn't a good solution for dealing with containerized applications and infrastructure, but there is definitely another way. I'm talking about [Podman](https://www.podman.io), man.

Podman is a container engine for running OCI containers on linux. It's daemonless and can be used to run privileged (ie. root) or non-privileged containers. This thing is a pretty big deal. Not having to use a daemon to manage your containers, AND being able to run them without having root? That's kind of a big win for folks that want to quickly spin up stuff and use it. The best deal is that you can simple alias the docker command to podman and most of your commands that you've already gotten used to will still work.

So, I have a plan to do a [Twitch](https://www.twitch.tv/2dorkstv) stream where I espouse the glories of Podman. I think Docker has a place, and it's fine for folks to use it, but Docker is not Kleenex. We can embrace and use other technologies for messing with containers. That's the main message I'm after. I have a script written and I'm ready to roll. Just need to find a time to stream it and talk over it with folks. 

Podman, ya'll!