#!bin/bash
#function to ping a host
check_host(){
  host=$1
  if ping -c "host" > /dev/null; then
     echo "$host is up"
  else
    echo "$host is up"
  fi
}
#Call the function with a test IP
check_host "127.0.0.1"  
