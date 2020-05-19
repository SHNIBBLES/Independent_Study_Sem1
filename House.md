* 2020-05-19: Homework assigned today:

  - Resolve the conflicts in House.md :-).

  - Please always always always always push after committing.  
    Don't wait until just before we get into Jitsi.  The sooner 
    I can see your code, the better prepared I can be.

  - Write doc strings for all functions and methods.

  - Add some unconditional debugging statements that print out at
    startup time and show the initial starting position and speed of
    each ball.  (Hint: you can do this by expanding the "__str__"
    method in the Ball class to have it include more information in
    addition to the Ball's ID).  

    The reason we want this initial debugging print is that it will
    allow me to save the exact starting state of all the balls -- so
    later, when I reproduce the buried-in-the-wall problem, I can at
    least tell you those starting positions etc, and we can make a way
    for you to take them as input so that you can run the program with
    the exact same starting state.

  - Conditionalize the other debugging statements (the ones already in
    the code right now), so that the user can press a key to turn them
    on or off.

  - Solve the ball-buried-in-the-wall problem (which I realize you
    can't reproduce yet, but see my earlier point about that).

* 2020-05-14: Homework assigned today:

  - Spawning code should be aware of where other balls are being
    spawned and avoid collisions.

  - Fix the bounce bug that shows up frequently with 5 balls
    (and also shows up with lower numbers of balls, though
    less frequently).

  - Karl to explain to Eli commands need "./" on the front
    (next time, because)

* 2020-05-10: Homework assigned today:

  - Make the balls bounce off each other.

  - Maybe do fancy wall-bounce behavior too, if time.

  - Maybe read a number higher than 9, if time.

* 2020-05-04: Homework assigned today:

              - Make the number of balls be an argument to the program.

              - Just do simple bouncing, not fancy bouncing.

              - Make screen Surface size be dynamic, based on real screen size.

              - Allow user to quit by typing 'q'.

* 2020-04-25: Eli completed the 2020-04-22 homework.
              Then we got the ball rotating in place.

              Assigned today: Eli will make the ball travel around and
              bounce off the sides of the window while rotating.

* 2020-04-22: Eli to learn the meaning of everything in the 1st example
              on https://www.pygame.org/docs/tut/PygameIntro.html and be
              able to explain it.  If have extra time, make eliGame.py
              do more (like move the circle, or expand it, etc).
