# twoot

Just a super simple python script to send some text to twitter and mastodon at the same time via CLI.
Checks character length to make sure its under 280 for twitter.

Requirements: 
* `pip install Mastodon.py tweepy`

Usage: 
* `./twoot.py "twoot test 🐦🐘"`

Add a symlink for convenience:
* `sudo ln -s /your-path/twoot/twoot.py /usr/local/bin/twoot`
*  `twoot "twoot test 🐦🐘"`
