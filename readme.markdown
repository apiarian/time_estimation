time_estimation
===============

A simple command line utility written in python3 which helps estimate the time
required to complete a task.

time_estimation.py
------------------

This script allows the user to enter the total number of items to be done
(number of paper cranes to be folded, 100 for a percentage based system, or
anything else that make sense). The current quantity is then set, either
directly with the update command or by delta using the increment command. The
status command prints the current state of the task. The help command provides
some extra information regarding the available commands. The session may be
restarted using the reset command or halted using the exit command.

This script is probably most useful for tasks that are repetitive and have a
consistent execution rate.

Licensing
---------

You may do what you wish with this code, but please attribute the author if you
do use it. No guarantees of usefulness or buglessness are provided.

Suggestions and patches are welcome.
