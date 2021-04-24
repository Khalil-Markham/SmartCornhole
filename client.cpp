#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <errno.h>
#include <netdb.h>
#include <cstdio>

// make the raspberry pi the master
// have the second raspberry pi always listening from the master pi as the server and updte its score



using namespace std;

void error(const char *msg){
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[]){
    int mysocket, n_port, r-port, numChars;
    socklen_t length;
    struct sockaddr)in serverAddress, server 1 from;
    struct hostent *server;
}

