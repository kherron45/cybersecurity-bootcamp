
#!/bin/bash
# guided lab: Loop through log files
for file in *.log; do
    if [ -f "$file" ]; then
        echo "Processing $files"
        grep "error" "$file" | head -n 2
    fi
done   

