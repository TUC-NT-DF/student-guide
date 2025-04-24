# Common pitfalls and how to avoid them

!!! notice
    **This page is used to document mistakes/pitfalls which happen often or are hard to spot or both.**

## Case 1

### When

During porting a link node [ld-node-avt-cam](https://gitlab.com/link.developers/ld-node-avt-camera) to link2. Seen [here](https://gitlab.com/link.developers/ld-node-camera-avt-2).

### What was the task

To get an IP camera up and running. The Allied Vision Cameras had to be indirectly connected to a laptop (via a network switch). The laptop and the camera need to be on the same network.

### Where it was stuck

The set-up described above was done and then I attempted to start the link node, but got no result. On Windows everything was fine but on Linux it wouldn't work. The camera was pingable but wasn't responding to UDP commands being sent from the laptop in the proprietary protocol. Tried complicated stuff like analysing the packets in Wireshark. This didn't help.

### What was missed and why

Role of netmask was ignored because it was wrongly assumed to be unimportant or insignificant.
Steps to change the IP address and netmask were followed for the laptop, however, it was missed that not only the camera had a different netmask (due to lack of configuration) (255.255.0.0 instead of 255.255.255.0) but also the fact that the camera IP and netmask can be changed using the native application provided by the manufacturer. Also, the device was not tested on Windows to check behaviour there in the very beginning.

### How it was fixed

Was told to check basic stuff like IP and netmask.

### Why it went wrong

Superficial exposure and lack of interest in understanding the camera device lead to the device being improperly used. Lack of attention to detail.

### Lessons to be learned

It is easy to complicate things when we don't know the basics. Solving a problem often requires narrowing down the problem which requires specific knowledge, not extra tools. Extra tools will make the problem more complex. Admitting lack of knowledge of basic things (in this case netmask configuration) will lead to a narrowing/funneling of the problem. Don't throw tools at problems, throw thorough understanding of basics instead. This is the right way to solve a problem.


## Case 2

### When

During adding a new project to the gitlab repository for the first time.

### What was the task

To add the source code to the gitlab repository.

### Where it was stuck

After adding the project to gitlab, the CI pipeline wouldn't start.

### What was missed and why

Adding the hidden files like .gitlab-ci-yml because a `git add *` does not automatically add those files to the index.

### How it was fixed

Was asked to check things on my side when the CI pipeline wouldn't start.

### Why it went wrong

Lack of attention to detail and overcondifence in the fact that "I did everything right".

### Lessons to be learned

There are two parts to this. First being that; sometimes it is easy to fall into a pattern (in this case `git add --> git commit --> expectation that everything is okay`) and to believe that there is nothing more to check and asking others to check things on their side. This is not right because there can always be subtle differences and it is always a good idea to double check on your own side before asking others. Second, it is important to recollect and retrace your steps while doing something second (or third usw) time because it is possible that you left out some small but critical step along the way. When we do something repeatedly, we slowly (and quite naturally) gain more and more confidence that we are doing things right and we are less and less skeptical of our performance. But this is kind of a fallacy. If mistake was made once, it can be easily made again (for the same reason it was made before) and it is a good idea to recollect "what went wrong" the first time one more time.
