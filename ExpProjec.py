- Create an EC2 instance by selecting the AMI ( devops-practice)
username and password based
---------------------------
RHEL9 -> Latest redhat enterprise OS
CentOS 9
RHEL9 == CentOS9

ec2-user
DevOps321
AMI --> devops-practice --> us-east-1 region

$ ssh ec2-user@3.92.185.67
$ password : DevOps321

## 
Installing My SQL : 

Install MySQL Server 8.0.x

Yum and Dnf both are same so , from RHL 9 we are using insted of Yum 

$ dnf install mysql-server -y # Option Y means by deafult we are giving go ahead permision

So we need sudo access to install this 

Start MySQL Service with below comamnds

$ systemctl enable mysqld
$ systemctl start mysqld


52.201.234.196 | 172.31.90.74 | t2.micro | null
[ root@ip-172-31-90-74 ~ ]# systemctl enable mysqld
Created symlink /etc/systemd/system/multi-user.target.wants/mysqld.service → /usr/lib/systemd/system/mysqld.service.

52.201.234.196 | 172.31.90.74 | t2.micro | null
[ root@ip-172-31-90-74 ~ ]# systemctl start mysqld

[ root@ip-172-31-90-74 ~ ]# systemctl status mysqld  # This will gives the status of mysqld server status
● mysqld.service - MySQL 8.0 database server
     Loaded: loaded (/usr/lib/systemd/system/mysqld.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-04-19 05:41:18 UTC; 56s ago
    Process: 1812 ExecStartPre=/usr/libexec/mysql-check-socket (code=exited, status=0/SUCCESS)
    Process: 1834 ExecStartPre=/usr/libexec/mysql-prepare-db-dir mysqld.service (code=exited, status=0/SUCCESS)
   Main PID: 1906 (mysqld)
     Status: "Server is operational"
      Tasks: 38 (limit: 4300)
     Memory: 395.6M
        CPU: 5.060s
     CGroup: /system.slice/mysqld.service
             └─1906 /usr/libexec/mysqld --basedir=/usr

Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1861]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/bin/sed]: sed s/^Group=//
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1860]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/bin/systemctl]: systemctl show -p Group …ld.service
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1862]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/bin/dirname]: dirname /var/log/mysql/mysqld.log
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1863]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/bin/dirname]: dirname /var/log/mysql/mysqld.log
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1866]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/bin/grep]: grep -v -e ^lost+found$ -e \.…h_history$
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1867]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/bin/ls]: ls -1A /var/lib/mysql
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal mysql-prepare-db-dir[1834]: Initializing MySQL database
Apr 19 05:41:07 ip-172-31-90-74.ec2.internal snoopy[1868]: [uid:27 sid:1834 tty:(none) cwd:/ filename:/usr/libexec/mysqld]: /usr/libexec/mysqld --i…user=mysql
Apr 19 05:41:17 ip-172-31-90-74.ec2.internal snoopy[1906]: [uid:27 sid:1906 tty:(none) cwd:/ filename:/usr/libexec/mysqld]: /usr/libexec/mysqld --basedir=/usr
Apr 19 05:41:18 ip-172-31-90-74.ec2.internal systemd[1]: Started MySQL 8.0 database server.
Hint: Some lines were ellipsized, use -l to show in full.
 

52.201.234.196 | 172.31.90.74 | t2.micro | null
[ root@ip-172-31-90-74 ~ ]# netstat -lntp   # This will give the port of mysqld application ( 33060 - by default )
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1245/sshd: /usr/sbi 
tcp6       0      0 :::33060                :::*                    LISTEN      1906/mysqld         
tcp6       0      0 :::22                   :::*                    LISTEN      1245/sshd: /usr/sbi 
tcp6       0      0 :::3306                 :::*                    LISTEN      1906/mysqld         

52.201.234.196 | 172.31.90.74 | t2.micro | null
[ root@ip-172-31-90-74 ~ ]# 


#### 

Set password for the root user in mysql db 

[ root@ip-172-31-90-74 ~ ]# mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.36 Source distribution

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 


mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

mysql> 





BackEnd : 

Warning: Permanently added '54.227.215.240' (ECDSA) to the list of known hosts.
ec2-user@54.227.215.240's password: 

██████╗ ██╗  ██╗███████╗██╗          █████╗
██╔══██╗██║  ██║██╔════╝██║         ██╔══██╗
██████╔╝███████║█████╗  ██║         ╚██████║
██╔══██╗██╔══██║██╔══╝  ██║          ╚═══██║
██║  ██║██║  ██║███████╗███████╗     █████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚════╝

Disclaimer:

This image is designed for only for the lab purpose
of learning DevOps and not recommended at all to use
in production or any company environments.


54.227.215.240 | 172.31.88.183 | t2.micro | null
[ ec2-user@ip-172-31-88-183 ~ ]$ 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ ec2-user@ip-172-31-88-183 ~ ]$ 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ ec2-user@ip-172-31-88-183 ~ ]$ dnf module disable nodejs -y
Error: This command has to be run with superuser privileges (under the root user on most systems).

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ ec2-user@ip-172-31-88-183 ~ ]$ sudo su -

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# dnf module disable nodejs -y
Extra Packages for Enterprise Linux 9 - x86_64                                                                                 17 MB/s |  21 MB     00:01    
Extra Packages for Enterprise Linux 9 openh264 (From Cisco) - x86_64                                                          2.6 kB/s | 2.5 kB     00:00    
Red Hat Enterprise Linux 9 for x86_64 - AppStream from RHUI (RPMs)                                                             37 MB/s |  31 MB     00:00    
Red Hat Enterprise Linux 9 for x86_64 - BaseOS from RHUI (RPMs)                                                                36 MB/s |  19 MB     00:00    
Red Hat Enterprise Linux 9 Client Configuration                                                                                19 kB/s | 2.4 kB     00:00    
Dependencies resolved.
==============================================================================================================================================================
 Package                               Architecture                         Version                               Repository                             Size
==============================================================================================================================================================
Disabling modules:
 nodejs                                                                                                                                                      

Transaction Summary
==============================================================================================================================================================

Complete!

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# dnf module enable nodejs:20 -y
Last metadata expiration check: 0:00:29 ago on Fri Apr 19 05:55:50 2024.
Dependencies resolved.
==============================================================================================================================================================
 Package                               Architecture                         Version                               Repository                             Size
==============================================================================================================================================================
Enabling module streams:
 nodejs                                                                     20                                                                               

Transaction Summary
==============================================================================================================================================================

Complete!

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# dnf install nodejs -y
Last metadata expiration check: 0:00:41 ago on Fri Apr 19 05:55:50 2024.
Dependencies resolved.
==============================================================================================================================================================
 Package                      Architecture       Version                                                         Repository                              Size
==============================================================================================================================================================
Installing:
 nodejs                       x86_64             1:20.11.1-1.module+el9.3.0+21385+bac43d5a                       rhel-9-appstream-rhui-rpms              14 M
Installing weak dependencies:
 nodejs-docs                  noarch             1:20.11.1-1.module+el9.3.0+21385+bac43d5a                       rhel-9-appstream-rhui-rpms             8.2 M
 nodejs-full-i18n             x86_64             1:20.11.1-1.module+el9.3.0+21385+bac43d5a                       rhel-9-appstream-rhui-rpms             8.5 M
 npm                          x86_64             1:10.2.4-1.20.11.1.1.module+el9.3.0+21385+bac43d5a              rhel-9-appstream-rhui-rpms             2.5 M

Transaction Summary
==============================================================================================================================================================
Install  4 Packages

Total download size: 33 M
Installed size: 175 M
Downloading Packages:
(1/4): nodejs-full-i18n-20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64.rpm                                                     19 MB/s | 8.5 MB     00:00    
(2/4): nodejs-docs-20.11.1-1.module+el9.3.0+21385+bac43d5a.noarch.rpm                                                          13 MB/s | 8.2 MB     00:00    
(3/4): npm-10.2.4-1.20.11.1.1.module+el9.3.0+21385+bac43d5a.x86_64.rpm                                                         12 MB/s | 2.5 MB     00:00    
(4/4): nodejs-20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64.rpm                                                               15 MB/s |  14 MB     00:00    
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                          35 MB/s |  33 MB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                      1/1 
  Installing       : nodejs-docs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.noarch                                                                         1/4 
  Installing       : nodejs-full-i18n-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64                                                                    2/4 
  Installing       : npm-1:10.2.4-1.20.11.1.1.module+el9.3.0+21385+bac43d5a.x86_64                                                                        3/4 
  Installing       : nodejs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64                                                                              4/4 
  Running scriptlet: nodejs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64                                                                              4/4 
  Verifying        : nodejs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64                                                                              1/4 
  Verifying        : nodejs-docs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.noarch                                                                         2/4 
  Verifying        : nodejs-full-i18n-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64                                                                    3/4 
  Verifying        : npm-1:10.2.4-1.20.11.1.1.module+el9.3.0+21385+bac43d5a.x86_64                                                                        4/4 

Installed:
  nodejs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64                         nodejs-docs-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.noarch               
  nodejs-full-i18n-1:20.11.1-1.module+el9.3.0+21385+bac43d5a.x86_64               npm-1:10.2.4-1.20.11.1.1.module+el9.3.0+21385+bac43d5a.x86_64              

Complete!

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# useradd expense

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# echo $?
0

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# mkdir /app

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# curl -o /tmp/backend.zip https://expense-builds.s3.us-east-1.amazonaws.com/expense-backend-v2.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3162  100  3162    0     0  14571      0 --:--:-- --:--:-- --:--:-- 14504

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 ~ ]# cd /app

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# unzip /tmp/backend.zip
Archive:  /tmp/backend.zip
  inflating: DbConfig.js             
  inflating: TransactionService.js   
  inflating: index.js                
  inflating: package.json            
   creating: schema/
  inflating: schema/backend.sql      

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# cd /app

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# npm install

added 82 packages, and audited 83 packages in 5s

12 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
npm notice 
npm notice New minor version of npm available! 10.2.4 -> 10.5.2
npm notice Changelog: https://github.com/npm/cli/releases/tag/v10.5.2
npm notice Run npm install -g npm@10.5.2 to update!
npm notice 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# pwd
/app

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# vim /etc/systemd/system/backend.service

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl daemon-reload

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl start backend

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl enable backend
Created symlink /etc/systemd/system/multi-user.target.wants/backend.service → /etc/systemd/system/backend.service.

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl status
● ip-172-31-88-183.ec2.internal
    State: degraded
    Units: 322 loaded (incl. loaded aliases)
     Jobs: 0 queued
   Failed: 1 units
    Since: Fri 2024-04-19 05:54:10 UTC; 26min ago
  systemd: 252-18.el9
   CGroup: /
           ├─init.scope
           │ └─1 /usr/lib/systemd/systemd --switched-root --system --deserialize 31
           ├─system.slice
           │ ├─NetworkManager.service
           │ │ └─1162 /usr/sbin/NetworkManager --no-daemon
           │ ├─amazon-ssm-agent.service
           │ │ └─1236 /usr/bin/amazon-ssm-agent
           │ ├─auditd.service
           │ │ └─912 /sbin/auditd
           │ ├─chronyd.service
           │ │ └─950 /usr/sbin/chronyd -F 2
           │ ├─crond.service
           │ │ ├─1245 /usr/sbin/crond -n
           │ │ └─1998 /usr/sbin/anacron -s
           │ ├─dbus-broker.service
           │ │ ├─934 /usr/bin/dbus-broker-launch --scope system --audit
           │ │ └─938 dbus-broker --log 4 --controller 9 --machine-id 6fd191fd77134c718be4bf9a7362db6a --max-bytes 536870912 --max-fds 4096 --max-matches 1310…
           │ ├─polkit.service
           │ │ └─952 /usr/lib/polkit-1/polkitd --no-debug
           │ ├─rsyslog.service
           │ │ └─1242 /usr/sbin/rsyslogd -n
           │ ├─sshd.service
           │ │ └─1243 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
           │ ├─system-getty.slice
           │ │ └─getty@tty1.service
           │ │   └─1258 /sbin/agetty -o "-p -- \\u" --noclear - linux
           │ ├─systemd-journald.service
           │ │ └─789 /usr/lib/systemd/systemd-journald
           │ ├─systemd-logind.service
           │ │ └─941 /usr/lib/systemd/systemd-logind
           │ ├─systemd-udevd.service
           │ │ └─udev
           │ │   └─808 /usr/lib/systemd/systemd-udevd
           │ └─udisks2.service
           │   └─942 /usr/libexec/udisks2/udisksd
           └─user.slice
             └─user-1001.slice
               ├─session-3.scope
               │ ├─1297 "sshd: ec2-user [priv]"
               │ ├─1309 "sshd: ec2-user@pts/0"
               │ ├─1310 -bash
               │ ├─1358 sudo su -
               │ ├─1359 su -
               │ ├─1360 -bash
               │ └─2166 systemctl status
               └─user@1001.service
                 └─init.scope
                   ├─1301 /usr/lib/systemd/systemd --user
                   └─1302 "(sd-pam)"

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl status backend
× backend.service - Backend Service
     Loaded: loaded (/etc/systemd/system/backend.service; enabled; preset: disabled)
     Active: failed (Result: exit-code) since Fri 2024-04-19 06:19:34 UTC; 1min 5s ago
   Duration: 377ms
   Main PID: 2123 (code=exited, status=1/FAILURE)
        CPU: 356ms

Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]:   code: 'ER_ACCESS_DENIED_ERROR',
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]:   errno: 1045,
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]:   sqlState: '28000',
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]:   sqlMessage: "Access denied for user 'expense'@'ip-172-31-88-183.ec2.internal' (using…rd: YES)",
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]:   sql: undefined,
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]:   fatal: true
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]: }
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal backend[2123]: Node.js v20.11.1
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal systemd[1]: backend.service: Main process exited, code=exited, status=1/FAILURE
Apr 19 06:19:34 ip-172-31-88-183.ec2.internal systemd[1]: backend.service: Failed with result 'exit-code'.
Hint: Some lines were ellipsized, use -l to show in full.

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# dnf install mysql -y
Red Hat Enterprise Linux 9 for x86_64 - AppStream from RHUI (RPMs)                                                             53 kB/s | 4.5 kB     00:00    
Red Hat Enterprise Linux 9 for x86_64 - BaseOS from RHUI (RPMs)                                                                57 kB/s | 4.1 kB     00:00    
Red Hat Enterprise Linux 9 Client Configuration                                                                                24 kB/s | 1.5 kB     00:00    
Dependencies resolved.
==============================================================================================================================================================
 Package                                      Architecture             Version                             Repository                                    Size
==============================================================================================================================================================
Installing:
 mysql                                        x86_64                   8.0.36-1.el9_3                      rhel-9-appstream-rhui-rpms                   2.7 M
Installing dependencies:
 mariadb-connector-c-config                   noarch                   3.2.6-1.el9_0                       rhel-9-appstream-rhui-rpms                    11 k
 mysql-common                                 x86_64                   8.0.36-1.el9_3                      rhel-9-appstream-rhui-rpms                    78 k

Transaction Summary
==============================================================================================================================================================
Install  3 Packages

Total download size: 2.8 M
Installed size: 60 M
Downloading Packages:
(1/3): mariadb-connector-c-config-3.2.6-1.el9_0.noarch.rpm                                                                    158 kB/s |  11 kB     00:00    
(2/3): mysql-common-8.0.36-1.el9_3.x86_64.rpm                                                                                 992 kB/s |  78 kB     00:00    
(3/3): mysql-8.0.36-1.el9_3.x86_64.rpm                                                                                         13 MB/s | 2.7 MB     00:00    
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                          12 MB/s | 2.8 MB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                      1/1 
  Installing       : mariadb-connector-c-config-3.2.6-1.el9_0.noarch                                                                                      1/3 
  Installing       : mysql-common-8.0.36-1.el9_3.x86_64                                                                                                   2/3 
  Installing       : mysql-8.0.36-1.el9_3.x86_64                                                                                                          3/3 
  Running scriptlet: mysql-8.0.36-1.el9_3.x86_64                                                                                                          3/3 
  Verifying        : mariadb-connector-c-config-3.2.6-1.el9_0.noarch                                                                                      1/3 
  Verifying        : mysql-8.0.36-1.el9_3.x86_64                                                                                                          2/3 
  Verifying        : mysql-common-8.0.36-1.el9_3.x86_64                                                                                                   3/3 

Installed:
  mariadb-connector-c-config-3.2.6-1.el9_0.noarch                mysql-8.0.36-1.el9_3.x86_64                mysql-common-8.0.36-1.el9_3.x86_64               

Complete!

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# mysql -h 172.31.90.74 -uroot -pExpenseApp@1 < /app/schema/backend.sql
mysql: [Warning] Using a password on the command line interface can be insecure.

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# echo $?
0

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# mysql -h 172.31.90.74 -uroot -pExpenseApp@1
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.36 Source distribution

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> show db;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'db' at line 1
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| transactions       |
+--------------------+
5 rows in set (0.00 sec)

mysql> exit
Bye

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl restart backend

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# $?
-bash: 0: command not found

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# echo $?
127

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# systemctl status backend
● backend.service - Backend Service
     Loaded: loaded (/etc/systemd/system/backend.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-04-19 06:28:25 UTC; 41s ago
   Main PID: 2364 (node)
      Tasks: 7 (limit: 4300)
     Memory: 20.2M
        CPU: 408ms
     CGroup: /system.slice/backend.service
             └─2364 /bin/node /app/index.js

Apr 19 06:28:25 ip-172-31-88-183.ec2.internal systemd[1]: Started Backend Service.
Apr 19 06:28:25 ip-172-31-88-183.ec2.internal snoopy[2364]: [uid:1002 sid:2364 tty:(none) cwd:/ filename:/bin/node]: /bin/node /app/index.js
Apr 19 06:28:25 ip-172-31-88-183.ec2.internal backend[2364]: { "timestamp" : 1713508105, "msg" : "App Started on Port 8080" }

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# mysql -h 172.31.90.74 -uroot -pExpenseApp@1 < /app/schema/backend.sql
mysql: [Warning] Using a password on the command line interface can be insecure.

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# 

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# echo $?
0

54.227.215.240 | 172.31.88.183 | t2.micro | null
[ root@ip-172-31-88-183 /app ]# mysql -h 172.31.90.74 -uroot -pExpenseApp@1
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 8.0.36 Source distribution

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of thei
r respective
owners.





## Front End 

This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '3.87.13.63' (ECDSA) to the list of known hosts.
ec2-user@3.87.13.63's password: 

██████╗ ██╗  ██╗███████╗██╗          █████╗
██╔══██╗██║  ██║██╔════╝██║         ██╔══██╗
██████╔╝███████║█████╗  ██║         ╚██████║
██╔══██╗██╔══██║██╔══╝  ██║          ╚═══██║
██║  ██║██║  ██║███████╗███████╗     █████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚════╝

Disclaimer:

This image is designed for only for the lab purpose
of learning DevOps and not recommended at all to use
in production or any company environments.


3.87.13.63 | 172.31.87.232 | t2.micro | null
[ ec2-user@ip-172-31-87-232 ~ ]$ 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ ec2-user@ip-172-31-87-232 ~ ]$ dnf install nginx -y 
Error: This command has to be run with superuser privileges (under the root user on most systems).

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ ec2-user@ip-172-31-87-232 ~ ]$ systemctl enable nginx
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-unit-files ====
Authentication is required to manage system service or unit files.
Authenticating as: Local Maintenance User (maintuser)
Password: 
Password: 
[1]+  Stopped                 systemctl enable nginx

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ ec2-user@ip-172-31-87-232 ~ ]$ ^C

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ ec2-user@ip-172-31-87-232 ~ ]$ 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ ec2-user@ip-172-31-87-232 ~ ]$ sudo su - 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# dnf install nginx -y
Extra Packages for Enterprise Linux 9 - x86_64                                                                                 16 MB/s |  21 MB     00:01    
Extra Packages for Enterprise Linux 9 openh264 (From Cisco) - x86_64                                                          2.6 kB/s | 2.5 kB     00:00    
Red Hat Enterprise Linux 9 for x86_64 - AppStream from RHUI (RPMs)                                                             32 MB/s |  31 MB     00:00    
Red Hat Enterprise Linux 9 for x86_64 - BaseOS from RHUI (RPMs)                                                                33 MB/s |  19 MB     00:00    
Red Hat Enterprise Linux 9 Client Configuration                                                                                15 kB/s | 2.4 kB     00:00    
Dependencies resolved.
==============================================================================================================================================================
 Package                               Architecture              Version                                  Repository                                     Size
==============================================================================================================================================================
Installing:
 nginx                                 x86_64                    1:1.20.1-14.el9_2.1                      rhel-9-appstream-rhui-rpms                     40 k
Installing dependencies:
 nginx-core                            x86_64                    1:1.20.1-14.el9_2.1                      rhel-9-appstream-rhui-rpms                    574 k
 nginx-filesystem                      noarch                    1:1.20.1-14.el9_2.1                      rhel-9-appstream-rhui-rpms                     11 k
 redhat-logos-httpd                    noarch                    90.4-2.el9                               rhel-9-appstream-rhui-rpms                     18 k

Transaction Summary
==============================================================================================================================================================
Install  4 Packages

Total download size: 643 k
Installed size: 1.8 M
Downloading Packages:
(1/4): nginx-filesystem-1.20.1-14.el9_2.1.noarch.rpm                                                                          153 kB/s |  11 kB     00:00    
(2/4): nginx-1.20.1-14.el9_2.1.x86_64.rpm                                                                                     528 kB/s |  40 kB     00:00    
(3/4): redhat-logos-httpd-90.4-2.el9.noarch.rpm                                                                               1.7 MB/s |  18 kB     00:00    
(4/4): nginx-core-1.20.1-14.el9_2.1.x86_64.rpm                                                                                3.8 MB/s | 574 kB     00:00    
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                                         3.5 MB/s | 643 kB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                                                                      1/1 
  Running scriptlet: nginx-filesystem-1:1.20.1-14.el9_2.1.noarch                                                                                          1/4 
  Installing       : nginx-filesystem-1:1.20.1-14.el9_2.1.noarch                                                                                          1/4 
  Installing       : nginx-core-1:1.20.1-14.el9_2.1.x86_64                                                                                                2/4 
  Installing       : redhat-logos-httpd-90.4-2.el9.noarch                                                                                                 3/4 
  Installing       : nginx-1:1.20.1-14.el9_2.1.x86_64                                                                                                     4/4 
  Running scriptlet: nginx-1:1.20.1-14.el9_2.1.x86_64                                                                                                     4/4 
  Verifying        : nginx-1:1.20.1-14.el9_2.1.x86_64                                                                                                     1/4 
  Verifying        : nginx-core-1:1.20.1-14.el9_2.1.x86_64                                                                                                2/4 
  Verifying        : nginx-filesystem-1:1.20.1-14.el9_2.1.noarch                                                                                          3/4 
  Verifying        : redhat-logos-httpd-90.4-2.el9.noarch                                                                                                 4/4 

Installed:
  nginx-1:1.20.1-14.el9_2.1.x86_64  nginx-core-1:1.20.1-14.el9_2.1.x86_64  nginx-filesystem-1:1.20.1-14.el9_2.1.noarch  redhat-logos-httpd-90.4-2.el9.noarch 

Complete!

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# systemctl enable nginx
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /usr/lib/systemd/system/nginx.service.

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# systemctl start nginx

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# rm -rf /usr/share/nginx/html/*

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# curl -o /tmp/frontend.zip https://expense-builds.s3.us-east-1.amazonaws.com/expense-frontend-v2.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  729k  100  729k    0     0  2859k      0 --:--:-- --:--:-- --:--:-- 2848k

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 ~ ]# cd /usr/share/nginx/html

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# unzip /tmp/frontend.zip
Archive:  /tmp/frontend.zip
  inflating: asset-manifest.json     
  inflating: index.html              
  inflating: robots.txt              
   creating: static/
   creating: static/css/
  inflating: static/css/main.b20b6ac4.css.map  
  inflating: static/css/main.b20b6ac4.css  
   creating: static/js/
  inflating: static/js/main.bcd36112.js.map  
  inflating: static/js/787.1f63e066.chunk.js.map  
  inflating: static/js/main.bcd36112.js.LICENSE.txt  
  inflating: static/js/main.bcd36112.js  
  inflating: static/js/787.1f63e066.chunk.js  
   creating: static/media/
  inflating: static/media/3TierArch.0486e7150e53d305d1c2-old.png  
  inflating: static/media/3TierArch.0486e7150e53d305d1c2.png  

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# vim /etc/nginx/default.d/expense.conf

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# systemctl restart nginx

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# systemctl system status
Unknown command verb system.

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: disabled)
     Active: active (running) since Fri 2024-04-19 07:09:13 UTC; 47s ago
    Process: 1709 ExecStartPre=/usr/bin/rm -f /run/nginx.pid (code=exited, status=0/SUCCESS)
    Process: 1710 ExecStartPre=/usr/sbin/nginx -t (code=exited, status=0/SUCCESS)
    Process: 1711 ExecStart=/usr/sbin/nginx (code=exited, status=0/SUCCESS)
   Main PID: 1712 (nginx)
      Tasks: 2 (limit: 4300)
     Memory: 2.2M
        CPU: 90ms
     CGroup: /system.slice/nginx.service
             ├─1712 "nginx: master process /usr/sbin/nginx"
             └─1716 "nginx: worker process"

Apr 19 07:09:13 ip-172-31-87-232.ec2.internal systemd[1]: Starting The nginx HTTP and reverse proxy server...
Apr 19 07:09:13 ip-172-31-87-232.ec2.internal snoopy[1709]: [uid:0 sid:1709 tty:(none) cwd:/ filename:/usr/bin/rm]: /usr/bin/rm -f /run/nginx.pid
Apr 19 07:09:13 ip-172-31-87-232.ec2.internal snoopy[1710]: [uid:0 sid:1710 tty:(none) cwd:/ filename:/usr/sbin/nginx]: /usr/sbin/nginx -t
Apr 19 07:09:13 ip-172-31-87-232.ec2.internal nginx[1710]: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
Apr 19 07:09:13 ip-172-31-87-232.ec2.internal nginx[1710]: nginx: configuration file /etc/nginx/nginx.conf test is successful
Apr 19 07:09:13 ip-172-31-87-232.ec2.internal snoopy[1711]: [uid:0 sid:1711 tty:(none) cwd:/ filename:/usr/sbin/nginx]: /usr/sbin/nginx
Apr 19 07:09:13 ip-172-31-87-232.ec2.internal systemd[1]: Started The nginx HTTP and reverse proxy server.

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# netstat -ntpl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      1712/nginx: master  
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1242/sshd: /usr/sbi 
tcp6       0      0 :::80                   :::*                    LISTEN      1712/nginx: master  
tcp6       0      0 :::22                   :::*                    LISTEN      1242/sshd: /usr/sbi 

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# ps -ef | gerp nginx
-bash: gerp: command not found

3.87.13.63 | 172.31.87.232 | t2.micro | null
[ root@ip-172-31-87-232 /usr/share/nginx/html ]# 

