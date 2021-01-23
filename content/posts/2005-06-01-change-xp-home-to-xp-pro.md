---
author: 2dsteve_ty3fxq
date: 2005-06-01 13:30:00+00:00
draft: false
title: Change XP Home to XP Pro
type: post
url: /2005/06/01/change-xp-home-to-xp-pro/
---

I ran across this really cool hack today and I thought I would share it with the world. Apparently it doesn't take much to change Windows XP Home Edition into the Pro Edition. I'm going to try this soon and let you all know how it goes.

1. Copy the root directory and the i386 directory of the WindowsXP CD to your harddisk   

2. Extract the Bootsector of your WindowsXP CD

   

3. Change 2 Bytes in i386\Setupreg.hiv :
   a) Open Regedit
   b) Highlight HKEY_LOCAL_MACHINE
   c) Menu: File -> Load Structure -> i386\Setupreg.hiv
   d) Assign an arbitrary name to the imported structure e.g. “Homekey”
   e) Goto HKEY_LOCAL_MACHINE\Homekey\ControlSet001\Services\setupdd
   f) edit the binary key “default” and change “01” to “00” and “02” to
   “00”
   g) Highlight “Homekey” and select menu: File -> unload structure
   4. Burn your new XP Pro CD
   5. Install WindowsXP as usual. Your XP Home Key will work.


If you do this, you might not be able to install Service Pack 2. You might be able to slipstream Service Pack 2 into the install disk but it hasn't been tried yet as far as I know. I'll give it a shot though and see what happens. Check out the full article [here](http://www.gizmodo.com/gadgets/software/howto-change-windows-xp-home-to-windows-xp-pro-105486.php).
