import os   #import operatig systems for pyth module
from socketserver import ThreadingMixIn  #import threading 
from xmlrpc.server import SimpleXMLRPCServer #import xmlrmpc server funcxtion 
from src.client import client #import client 
import random  #import random 
class MultiThreadedSimpleXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

vector_clock = []#function for vector clock
each_port = 0 #single port
clock_log = 0 #function for clock
process_port_nos = [] #multiple ports

def increment_vect_clk():  #function to increment the vector clock 
    global vector_clock     #declaration of vector_clock var 
    index_port = get_index_port() #port index function to get the port index 
    vector_clock[index_port] += 1 #vector clock incrementation using the port index 
    return

def get_index_port(): #function to get the port index 
    global each_port, process_port_nos  #variables declaration for single and multiple ports
    for i, port_one in enumerate(process_port_nos):  #for first port in all these processes
        if port_one == each_port: #if first port is equal to the port given 
            return i   #return 
    raise Exception("port for process not found in the set of ports") #excepytion if the port not found
    return

def update_vector_clock(vector):  #update the vector clock function after message
    global vector_clock       #vector clock declaration
    if (len(vector) != len(vector_clock)): #if the length of the vector is not equal to the length of the vector clock 
        raise Exception("vector size mismatch")   #raisedddd excetion for vector mismatch
    vector_clock = [max(v1,v2) for v1,v2 in zip(vector, vector_clock)]  #if the vector clock is  in zip of vector and vector clock 
    return

def start_sync(): #initialize synchronization
    global process_port_nos #declaration of ports
    proxies = [client.get_proxy(x) for x in process_port_nos] #proxies for the ports
    log_clocks = [proxy.get_logical_clock() for proxy in proxies] #get the proxy function using clock 
    avg_clk = int(sum(log_clocks)/len(log_clocks)) #using the func with the formual
    [proxy.synchronize_clock(avg_clk, len(process_port_nos)) for proxy in proxies]#proxy clock for synch using clk
    return

def get_logical_clock():  #get function for the clock 
    global clock_log #glb declaration of the  variable
    return clock_log #return function for the clock

def msg_incoming(vector):  #incomming msg function 
    global each_port  #declaring the variable port
    print(f"process node on port {each_port} received a message")  #process node function for the message received 
    print_vector_clock()#print vectclk func call
    increment_vect_clk()#increment vectclk func call
    update_vector_clock(vector) #update vectclk function call using the vector
    print_vector_clock() #calling the printvector clock function
    return

def print_logical_clock(): #print function
    #print(f"logical clock for {each_port}: {clock_log}")
    return #return val

def synchronize_clock(counter_flag, n): #synchclock for this one 
    global vector_clock #vect clk declaration
    global clock_log  #declaration of function
    clock_log = counter_flag #calling the counter_flag
    vector_clock = [counter_flag for x in range(n)] #vector_clock range
    print_logical_clock() #print the function call
    return

def initialize_logclock(): #initialize funtion
    global clock_log #declaring the variable here 
    clock_log = random.randint(1, 10)  #initializing some integer for this function
    return

def msg_outgoing(receiver_port): #outgoing msg function declaration using the target port
    global each_port, vector_clock #declaration of vars using port and vectclk
    print_vector_clock()  #calling the print func
    increment_vect_clk() #incrementing the vect clk func call
    proxy = client.get_proxy(receiver_port) ##get port func
    proxy.msg_incoming(vector_clock) #get proxy for the incomming msg func
    print(f"process node on port {each_port} sent a message")  #prcess node sent a msg function
    print_vector_clock()#pprint vect func call
    return

def print_vector_clock(): #print vector clock function 
    print(f"vector clock for {each_port}: {vector_clock}") #for the single port print the function
    return

def server_start(server_data): #func to start server function declaration 
    global each_port, process_port_nos # declaration of teh global variables
    each_port, process_port_nos = server_data #single port and  multiple ports
    initialize_logclock() #initialize the clock
    print_logical_clock()   #print func for the clock
    with MultiThreadedSimpleXMLRPCServer(('localhost', each_port), allow_none= True) as server: #with the thraeding server
        server.register_introspection_functions() #server functions
        server.register_function(synchronize_clock) #server reg functions 
        server.register_function(get_logical_clock) #ser reg function for the lgclk
        server.register_function(start_sync)#initialze synch for gthe clk
        server.register_function(msg_incoming) #for the incomming msg and 
        server.register_function(msg_outgoing) #fr the outgoing msg
        print(f"server is serving on port {each_port}") #server print
        server.serve_forever() #server func
    return



    
