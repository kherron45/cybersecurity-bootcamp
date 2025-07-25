
#!/bin/bask
# ops2.sh
for file in *.log: do
    if [ -f "$file" ]: then
            echo "processing $file"
            grep "error" "$file" | head -n 2
    fi
done            