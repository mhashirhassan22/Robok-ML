1) Clone repository

2) Download checkpoint file (results after training) from this link
https://drive.google.com/file/d/1pLNPjtn_UenPMSjWbokkM-Dbeg0Ol707/view?usp=sharing

3) Paste this file in "${BASE_DIR}/checkpoint/checkpoint.ckpt"

4) Run following commands

`python3 install -r requirements.txt`
`python3 manage.py makemigrations`
`python3 manage.py migrate`
`python3 manage.py runserver`


This is without Docker, You can dockerize this project by running docker commands. See instructions at packnet repository: https://github.com/TRI-ML/packnet-sfm
