import socket
import sys
import argparse
from threading import Thread, Lock
from queue import Queue

# define socket
# s = socket.socket()

# number of threads, can be tuned
N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()

# create a function to check the open ports
def port_scan(port):
    """
    Scan a port on the global variable `host`
    """
    try: # try-except block
        s = socket.socket() # create a socket object
        s.connect((host, port)) # connect object from socket object is passed host and port
    except: # exception for closed port
        with print_lock:
            print(f"{host:15}:{port:5} is closed", end='\r')
    else: # exception for open port
        with print_lock:
            print(f"{host:15}:{port:5} is open")
    finally:
        s.close()
# scan thread function
def scan_thread():
    global q # Queueing our ports is set as global
    while True: # while what is True?
        # get the port number from the que
        worker = q.get()
        # scan that port number
        port_scan(worker)
        # tells the queue that the scanning for that port
        # is done
        q.task_done()

def main(host, ports):
    global q
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon = True
        # start the daemon thread
        t.start()
    for worker in ports:
        # for each port, put that port into the queue
        # to start scanning
        q.put(worker)
    # wait the threads ( port scanners ) to finish
    q.join()
if __name__ == "__main__":
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Host to scan:")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65525 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [p for p in range(start_port, end_port)]

    main(host, ports)