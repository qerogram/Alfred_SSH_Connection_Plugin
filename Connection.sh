#!/usr/bin/expect
set timeout 180
set host [lindex $argv 0]
set port [lindex $argv 1]
set name [lindex $argv 2]
set password [lindex $argv 3]

spawn ssh $host -l $name -p $port
expect {
    "(yes/no)?" {
        send "yes\n"
        expect "password:"
        send "$password\n"
    }
    "password:" {
        send "$password\n"
    }
}

interact