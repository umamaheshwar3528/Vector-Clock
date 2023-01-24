import multiprocessing as mp     #multiprocessig for more than 1 processor
import threading                  #threads import
import random                    #import random
import time                      #import time 
from src.client import client    #import client server
from src.server.server import server_start #server impotrt function 

process_port_nos = [3900,3901,3902]   #ports to be used

def initialize_nodes():      #initialize_nodes function 
    global process_port_nos   #declaring the ports variable
    print("*****starting nodes******")  #starting the nodes
    with mp.Pool(processes=len(process_port_nos)) as pool: #length of ports as pool
            pool.map(server_start, [(x,process_port_nos) for x in process_port_nos]) #mapping the ports
    return

def echo(server_data):     #server_data function 
    each_port, process_port_nos = server_data   #for single and multiple ports 
    print(each_port, process_port_nos) #print the ports 
    return each_port       #returning the port

def trigger_message():       #trigger msg function 
    global process_port_nos  #declaration for [ports] 
    port_one = random.choice(process_port_nos) #first port
    port_two = other_port(port_one) 
    port_three=other_port(port_one  #second port
    proxy1 = client.get_proxy(port_one)     #declaring the proxy for client
    print("****** triggering a new message event *******")
    print(f"process node on port {port_one} is sending message to node on port {port_two}")  #sending message to the second port
    proxy1.msg_outgoing(port_two) #second port 
    return

def other_port(port_one): #get port function 
    global process_port_nos    #variable for ports 
    if len(process_port_nos) < 2:  #if length is less for ports 
        return
    port_two = random.choice(process_port_nos)   #second port for process 
    if port_two!= port_one:  #if second port is not equal to first port
        return port_two       #return second port 
    return other_port(port_one) #get different port

if __name__ == "__main__":#main function
    try:   #try 
        t1 = threading.Thread(target=initialize_nodes)  #declaring the t1 var
        t1.start()  #starting thread 1 
        time.sleep(1) #sleep for thread 1    
        random_port= random.choice(process_port_nos) #if the port is same 
        random_proxy = client.get_proxy(random_port) #proxy for rand port
        random_proxy.start_sync() #initialize synch
        trigger_message() #trigger message 
    except:
        print('exiting')#exit the app

    