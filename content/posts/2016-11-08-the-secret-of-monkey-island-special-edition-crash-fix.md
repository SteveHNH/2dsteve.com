---
author: 2dsteve_ty3fxq
date: 2016-11-08 13:09:58+00:00
draft: false
title: 'The Secret of Monkey Island: Special Edition Crash FIX'
type: post
url: /2016/11/08/the-secret-of-monkey-island-special-edition-crash-fix/
categories:
- Tech
---

I don't normally post this kind of thing on the blog, but I had such a hard time finding the fix for this that I felt compelled to put it up here.

I started up The Secret of Monkey Island: Special Edition for the first time in a long time the other day. Much to my dismay, it crashed on startup. I tried again. Crash! Nothing seemed to work. Googling the problem revealed that it is an issue that arose after Nvidia released the version 369 driver. I'm on 373 or something and I just didn't want to have to roll back.

If you are running into this problem, there is a really simple fix.

Download the [d3d9.dll](https://mods.curse.com/mods/skyrim/skyrim-better-performance) file and drop it in **<SteamLibrary>/steamapps/common/The Secret of Monkey Island** or whever your game directory is

That's all it takes! It fired up and worked like a charm. The file is used for better performance in Skyrim but it does the trick for this issue as well.

Here's a link to the file hosted on curse.com: [https://mods.curse.com/mods/skyrim/skyrim-better-performance](https://mods.curse.com/mods/skyrim/skyrim-better-performance)
