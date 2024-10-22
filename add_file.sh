#!/bin/bash


file_to_add="trian.py"  # replace with your actual file name


if [ -f "$file_to_add" ]; then
    
    git add "$file_to_add"

    
    git commit -m "Adding $file_to_add to the repository"

    
    git push origin master
else
    echo "File $file_to_add does not exist."
fi
