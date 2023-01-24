import os   #import operating systems 
import time  #import time 
import xmlrpc.client  #import client

def get_proxy(each_port):  #get proxy for the port
    server_uri = f"http://localhost:{each_port}"  #server uri for the port
    proxy = xmlrpc.client.ServerProxy(server_uri)  #proxy for the server uri
    return proxy #return proxy function
