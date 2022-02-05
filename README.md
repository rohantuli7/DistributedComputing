# Distributed Computing

Distributed computing concepts implemented in Python.

## RPC
* Practical implementation of RMI was done using python. Pyro4 is an inbuilt library which can be used to implement RMI. It is easier to implement RMI in a Java environment than python. The RMI (Remote Method Invocation) is an API that provides a mechanism to create distributed application in java. The RMI allows an object to invoke methods on an object running in another JVM. The RMI provides remote communication between the applications using two objects stub and skeleton.
* First, a localhost server is created. This local host server is linked to two files, namely; server.py & client.py. The server.py file acts as the recipient of the message sent by the client.py file thus, depicting Remote method invocation. There can be multiple clients, but only one server per name, so if you need multiple servers for some reason you’re going to need to register names with an identifier.

## RMI
* The concept of RMI for editing files on the server through a call made by the client. RMI allows an object to invoke methods on an object running in another virtual machine (ideally JVM). RMI provides remote communication between the applications using two objects stub and skeleton.
* An RMI application can be divided into two parts, Client program and Server program. A Server program creates some remote object, make their references available for the client to invoke method on it. A Client program make request for remote objects on server and invoke method on them. Stub and Skeleton are two important objects used for communication with remote object. RMI can be used for editing, deleted, transferring, inserting, etc. files and objects between the server and the client through the internet. 

## Berkeleys Algorithm
* Berkeley’s Algorithm is a clock synchronization technique used in distributed systems. The algorithm assumes that each machine node in the network either doesn’t have an accurate time source or doesn’t possess an UTC server.
* Often, any client whose clock differs by a value outside of a given tolerance is disregarded when averaging the results. This prevents the overall system time from being drastically skewed due to one erroneous clock. it is intended for use within intranets.

## Bully's or token ring algorithm
* Election algorithms choose a process from group of processors to act as a coordinator. If the coordinator process crashes due to some reasons, then a new coordinator is elected on other processor. Election algorithm basically determines where a new copy of coordinator should be restarted.
* In distributed computing, the bully algorithm is a method for dynamically electing a coordinator or leader from a group of distributed computer processes. The process with the highest process ID number from amongst the non-failed processes is selected as the coordinator.

## Consistency models
* Implementation of data consistency model was done using python. Socket programming has been used such that, we have simulated data consistency by following its fundamentals of maintaining consistency in read and write operations. A server and a client were used where each of them could monotonically read or monotonically write files separately.
* Monotonic reads ensure that if a process performs read r1, then r2, then r2 cannot observe a state prior to the writes which were reflected in r1; intuitively, reads cannot go backwards. Monotonic reads do not apply to operations performed by different processes, only reads by the same process.
Monotonic writes ensure that if a process performs write w1, then w2, then all processes observe w1 before w2. Monotonic writes do not apply to operations performed
by different processes, only writes by the same process.

## Client server communication
* Two different types of cipher techniques were implemented namely; 1. Substitution Cipher and 2. Transposition cipher. Both these techniques were implemented in python using socket programming where the client sent a .txt to the server and the server encrypted the .txt file data in accordance with the methods mentioned above. For this experiment, only lower-case alphabets have been considered.
1. Substitution Cipher: In this method, the client sent a .txt file to the server with a key. This key was later used by the server to apply mathematical operations or logic (in our case cyclic addition) to retrieve the pre-fed dictionary containing all the alphabets in an increasing order of their ascii values. The key was used to encrypt the data. This updated encrypted file was stored in the server. White spaces have been considered.
2. Transposition Cipher: In this method, the client sent a .txt file to the server. This .txt file was encrypted by the server by simply taking a transposition of the alphabets present in the file. This was done by storing each alphabet into a matrix after which, the transpose of the matrix was found and the updated .txt file was stored in the server. White spaces have not been considered and the empty space has been filled with $.

