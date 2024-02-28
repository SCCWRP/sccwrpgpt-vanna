#!/bin/bash
alias logs='sudo docker container logs -f ai-vanna-tool-empa';
alias restart='sudo docker container restart ai-vanna-tool-empa';
alias relog='sudo docker container restart ai-vanna-tool-empa;sudo docker container logs -f ai-vanna-tool-empa;';
alias clearlogs='sudo sh -c "echo \"\" > $(docker inspect --format='{{.LogPath}}' ai-vanna-tool-empa)"';
alias ipython='sudo docker container exec -it -w /var/www/sccwrpgpt/testing ai-vanna-tool-empa ipython';
