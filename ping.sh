nmap challenges.unitedctf.ca -p $(cat challenges/docker-compose.yml  | grep -P '[0-9]+:[0-9]+' | sed 's/[- "]//g' | cut -d ':' -f 1 | tr '\n' ',')
