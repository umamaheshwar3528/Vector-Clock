We have developed an n-node distributed system that implements a vector clock. The distributed system uses a logical clock to timestamp messages sent/received among the nodes.
To simplify the design and testing,the distributed system will be emulated using multiple processes on a single machine.
Each process represents a machine and has a unique port number for communication.
Created two threads for each process, one for sending messages to other nodes and one for listening to its communication port.
Communication among nodes can be done using RPC or using sockets. Once a process sends a message, it prints its vector clock before and after sending a message.
Similarly,once a process receives a message, it prints its vector clock before and after receiving the message.
The number of processes (machines) is fixed (equal to or larger than 3) and processes will not fail, join, or leave the distributed system.

How to run Code:
1.Open the command prompt for vector clock and run python app.py command. 
2. After the connection we can see all the time stamps that when the messages are sent and received.
