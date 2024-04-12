#!/usr/bin/env bash

STATE=$(amixer get Master | grep -oP '\[on\]' | wc -l)

if [ "$STATE" -eq 0 ]; then
  amixer set Master unmute
else
  amixer set Master mute
fi
