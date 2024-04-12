#!/usr/bin/env bash

# VOLUME=$(amixer get Master | 
# 	grep -oP '\d+%' | 
# 	head -n 1)
# VOLUME=${VOLUME::-1}
#
# if ["$VOLUME" -eq 0]; then
# 	amixer set Master on
# else
# 	amixer set Master off
# fi
#

STATE=$(amixer get Master | grep -oP '\[on\]' | wc -l)

if [ "$STATE" -eq 0 ]; then
  amixer set Master unmute
else
  amixer set Master mute
fi
