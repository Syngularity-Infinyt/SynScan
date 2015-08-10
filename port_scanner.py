from socket import *
import sys
import re

_ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")


def scan_single_port(target_host, target_port):
    try:
        connect_to_port = socket(AF_INET, SOCK_STREAM)
        connect_to_port.connect((target_host, target_port))
        print 'Connection to ' + target_host + ' port ' + str(target_port) + ' succeeded!'
        grab_port_type(connect_to_port)
        return True
    except Exception, e:
        print 'Unable to connect to', target_host + ':' + str(target_port), '\nError message:', e
        return False, e


def grab_port_type(connect_to_port):
    try:
        connect_to_port.send('Szia cica\r\n')
        ret = connect_to_port.recv(1024)
        print str(ret)
        return
    except Exception, e:
        print 'Unable to grab port info:', str(e)
        return


def port_scan(ip, from_port=0, to_port=None):

    if to_port is None:
        to_port = from_port + 100

    for port in range(from_port, to_port):
        scan_single_port(ip, port)


class Host:
    def __init__(self, host_name_or_ip):
        if _ip.match(host_name_or_ip):
            self.ip = host_name_or_ip
            try:
                self.host_name = gethostbyname(host_name_or_ip)
            except Exception, e:
                print 'Error:', e
                self.name = None
        else:
            try:
                self.ip = gethostbyaddr(host_name_or_ip)
            except Exception, e:
                print 'Unable to resolve host name'
                print 'Error message:', e


def main():
    try:
        host = Host(sys.argv[1])
    except Exception, e:
        print 'At least one argument need \n'
        exit(e)

    setdefaulttimeout(4)
    if len(sys.argv) == 4:
        from_port = int(sys.argv[2])
        to_port = int(sys.argv[3])
        port_scan(host.ip, from_port=from_port, to_port=to_port)
    elif len(sys.argv) == 3:
        from_port = int(sys.argv[2])
        port_scan(host.ip, from_port=from_port)
    elif len(sys.argv) == 2:
        port_scan(host.ip)


if __name__ == "__main__":
    main()
