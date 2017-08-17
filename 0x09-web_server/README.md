# Web server
![alt text](https://i.imgur.com/8Gu52Qv.png)
## Description
Configuring web-01 server, writung a Bash script that automatically performs commands to configure a Ubuntu machine without any human intervention
## Tasks

0. a Bash script that transfers a file from our client to a server:

Requirements:

1. Accepts 4 parameters:

   1) The path to the file to be transferred

   2) The IP of the server we want to transfer the file to

   3) The username scp connects with

   4) The path to the SSH private key that `scp` uses

2. Display Usage: 0-transfer_file `PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed

3. `scp` must transfer the file to the user home directory `~/`

4. Strict host key checking must be disabled when using `scp`


1. Install nginx web server

2. Setup a domain name

3. Configure your Nginx server so that /redirect_me is redirecting to another page.

4. Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page`

### __Clone repository:__ https://github.com/KatyaKalache/holberton-system_engineering-devops.git

## List of functions and system calls used

| What should I learn from this project |
| ---------------- |
|  What DNS stands for |
|  What is DNS main role |
|  What are DNS record types for: `A`, `CNAME`, `TXT`, `MX` |
|  What is the main role of a web server |

## Authors

Ekaterina Kalache: [github account](https://github.com/KatyaKalache), [twitter](https://twitter.com/KatyaKalache)

## License
Public, no copyright protection# holberton-system_engineering-devops
