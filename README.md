ten-second-balls
================

Ludum Dare 27 Entry by Iain Learmonth

Requires:

* Python 2.7
* pygame
* pymunk

On Debian like systems, the following should cover these:

    sudo apt-get install python27 python-pygame python-pip
    sudo pip install pymunk

The Story
---------

You're a person (blue ball) trapped in a maze that needs to reach the escape (yellow ball). Unfortunately, sometimes you need something to stand on and all that's available are a series of bombs (purple balls). As soon as you touch a bomb for the first time, it will active (red balls) and you'll have 10 seconds to get your use out of it and get away before it blows.

Note: Currently, there's no damage to the player from being near an exploded bomb. Time ran out before this could be developed.

How To Play
-----------

Information screens can be dismissed by the space bar. For everything else, use WASD. Make your way to the yellow ball to win.

It is possible to put yourself into an unwinnable situation. Just to frustrate you futher when this happens, you will have to restart the game.

Enjoy :)

Screenshots
-----------

See the screenshots/ folder.

License
-------

(C) Iain Learmonth 2013. All source code, documentation and assets for Ten Second Balls licensed under the GNU GPL version 2. See LICENSE for more details.

