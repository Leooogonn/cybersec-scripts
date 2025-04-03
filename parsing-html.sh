#!/bin/bash
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
LGREEN='\033[1;32m'
LGRAY='\033[1;37m'
CYAN='\033[1;36m'

if [ "$1" == "" ]
then
        echo -e "${YELLOW}========================================================${GREEN}"
        echo -e "#${CYAN}                    PARSING-HTML                      ${GREEN}#"
        echo -e "#${CYAN}       Modo de uso: $0 DOMINIO ${GREEN}        #"
        echo -e "#${CYAN}       Exemplo: $0 google.com.br ${GREEN}      #"
        echo -e "${YELLOW}========================================================"
else
        echo -e "${YELLOW}========================================${GREEN}"
        echo -e "*${LGREEN}          Buscando URLs...           ${GREEN} #"
        echo -e "${YELLOW}========================================${LGRAY}"
        wget -O lista.html $1 2>/dev/null;
        cat lista.html | grep "href=\"http" | cut -d "/" -f 3 | cut -d '"' -f 1 | grep ".com" | sort -u > lista.txt;
        cat lista.txt
        echo -e "${YELLOW}========================================${GREEN}"
        echo -e "*${LGREEN}          Buscando Hosts...          ${GREEN} #"
        echo -e "${YELLOW}========================================${LGRAY}"
        for host in $(cat ./lista.txt);
        do
        host $host | grep "has address" | cut -d " " -f 4 >> ip.txt;
        done
        sort -u ip.txt
        rm lista* ip.txt
        fi
