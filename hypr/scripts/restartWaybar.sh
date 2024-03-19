#!/bin/bash

_ps=(waybar)
for _prs in "${_ps[@]}"; do 
	if [[ `pidof ${_prs}` ]]; then 
		killall -9 ${_prs}
	fi
done

waybar -c ~/.config/waybar/config &
# waybar -c ~/.config/hypr/waybar/config &
