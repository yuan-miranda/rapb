### Remote Access Power Brick (RAPB)
Control the power brick (laptop charger) remotely using Arduino[<sup>1</sup>](https://en.wikipedia.org/wiki/Arduino) and a relay module[<sup>2</sup>](https://www.elprocus.com/5v-relay-module/) using serial communication interface[<sup>3</sup>](https://en.wikipedia.org/wiki/Serial_communication).

> [rapb.ino](src/rapb/rapb.ino) source code of the Arduino<br>
> [rapb.py](src/rapb.py) is the Python file used to communicate and send command to the Arduino

Commands:
- <b>on:</b> turn on the relay<br>
- <b>off:</b> turn off the relay<br>
- <b>status:</b> Get the status of the relay<br>
- <b>restart:</b> verbosed version of "off" command lol<br>
- <b>exit:</b> exit the script<br>
