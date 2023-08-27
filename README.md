### Remote Accessed Power Brick (RAPB)
Control the power brick (laptop charger) remotely using Arduino[<sup>1</sup>](https://en.wikipedia.org/wiki/Arduino) and a relay module[<sup>2</sup>](https://www.elprocus.com/5v-relay-module/) via serial communication interface[<sup>3</sup>](https://en.wikipedia.org/wiki/Serial_communication).

> [rapb.ino](src/rapb/rapb.ino) source code of the Arduino<br>
> [rapb.py](src/rapb.py) is the Python file used to communicate and send command to the Arduino

<pre>
Commands and Shortcuts:
on,            1 : Turn on the relay
off,           0 : Turn off the relay
status,  sts,  2 : Get the relay status
restart, res,  3 : Verbosed version of "off" command lol
exit,    quit, q : Exit the script
help,          h : Print the help page
</pre>
