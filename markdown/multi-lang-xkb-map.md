%%%
#How to set up Greek keyboard layout
%%%
##Replace system greek keymap
###Disclaimer:
I am not a native Greek speaker. I use Greek letters for math symbols, and the map that I replace here is apparently not an intuitive mapping if you actually speak the language. In that case, I recommend skipping the replacement of `/usr/share/X11/xkb/symbols/gr`, leaving the (probably better) system default.

That said, this keymap works well for me as an English speaker.

Download [gr.228.zip][1]

Back up system keymap

```
cd
mkdir keymapbackup
cp -v /usr/share/X11/xkb/symbols/gr keymapbackup/gr.backup
```

and move the new file into place

```
sudo cp -v gr.228/usr/share/X11/xkb/symbols/gr
```

##Edit xorg.conf.d
There are a couple of other ways to set the Greek keyboard from this point, but I use the `xorg.conf.d` method because it persists over reboots, and isn't user-specific.

Create `/etc/X11/xorg.conf.d/30-keyboard.conf` and give it contents:
%%%
```
Section "InputClass"
        Identifier "system-keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "us,gr"
        Option "XkbVariant" "mac,qwerty"
        Option "XkbOptions" "grp:caps_toggle"
EndSection
```
%%%

You may wish to use different values for "XkbVariant" and "XkbOptions" good luck on finding documentation on these. It seems that the convention for "XkbOptions" if you want a toggle is to use "grp:<keyname>_toggle". Naturally, the above configuration maps the CAPS lock key to toggle between us and gr keyboards.

Restart X, hit your key combo to switch layouts.

##Useful links:
[Xkb Unofficial Documentation][2]

[Another example configuration][3]

[1]: http://www.frame-poythress.org/wp-content/uploads/2013/01/gr.228.zip "Alternative Greek Keymap"
[2]: http://www.charvolant.org/~doug/xkb/html/index.html "Xkb Unofficial Documentation"
[3]: https://bbs.archlinux.org/viewtopic.php?id=152018 "Another example"