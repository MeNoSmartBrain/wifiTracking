#!/bin/bash

# Fake probe request
probequest --fake wlp0s20f3 -o $(pwd)/wifiData.csv

# Real probe request
# probequest wlp0s20f3 -o $(pwd)/result.csv