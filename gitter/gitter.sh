#!/bin/bash

date=`date -I`
echo $RANDOM > hit.txt
git commit -m "commit_message"
git push