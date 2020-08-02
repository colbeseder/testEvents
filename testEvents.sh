echo "Reading events from $1"
echo "Sending events to $2<event>$3"

cat $1 | grep -oP "\S+" | while read line ; do
    #echo "$2${line}$3"
    curl -I "$2${line}$3" 2> /dev/null | grep "HTTP/2 200" | if [ "$(</dev/stdin)" ]; then echo "$line" | tee -a unfiltered.txt ;  fi
done

echo "Done!"