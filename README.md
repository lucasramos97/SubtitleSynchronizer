## SubtitleSynchronizer

This is a script written in Python 3 that synchronizes captions in the terminal's .srt files. To use it, just run python3 by passing the file 'run.py' as parameters and defining whether to advance or reduce the subtitle time, for example: +2 or -2 (use '+' to advance, and '-' to delay) the value is set in seconds (2 seconds in this example). It is also necessary to add the content of the desynchronized subtitle in the file 'subtitle_not_synchronized.srt' after running the script the subtitle result will be in the file 'subtitle_synchronized.srt', just compile the content for the target subtitle. Complete example: python3 run.py -2 or python3 run.py +2.

## Author

This is a personal project of mine that i created so that it was not necessary to be searching for suitable subtitles to watch it, with it i can take any one, discover the difference in sync and run the script to run it.
