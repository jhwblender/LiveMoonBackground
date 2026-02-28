# LiveMoonBackground
Using NASA provided images to show the current phase of the moon as a desktop background

Instructions:
0: from inside the directory, run "pip install -r requirements.txt"
1: Seach on Google: "Moon Phase and Libration, (current year)"
2: Download the desired resolution Movie/video file
3: Put shared/default values in "config.ini"
4: Put your personal machine paths in "config.local.ini" (this file is gitignored)
5: Schedule to run on task scheduler to run at the start of the day, and repeat every hour for the duration of a day

Config behavior:
- The app always loads "config.ini".
- If "config.local.ini" exists, it is loaded after and overrides matching values.
- Keep personal absolute paths in "config.local.ini" so they never get committed.