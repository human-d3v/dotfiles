#!/bin/bash
# File: check_updates.sh

# Check for available updates
available_updates=$(pkcon get-updates -p | grep -c '^[a-zA-Z0-9]')

echo "$available_updates"
