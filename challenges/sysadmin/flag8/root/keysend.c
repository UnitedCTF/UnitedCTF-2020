#include <fcntl.h>
#include <unistd.h>
#include <netdb.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 

#define SA struct sockaddr 

int main() {
    int sockfd, connfd; 
    struct sockaddr_in servaddr, cli; 
  
    sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    if (sockfd == -1) { 
        printf("socket creation failed...\n"); 
        exit(1); 
    }
    bzero(&servaddr, sizeof(servaddr)); 
  
    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1"); 
    servaddr.sin_port = htons(1337); 
  
    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) { 
        printf("connection with the server failed...\n"); 
        exit(1); 
    }

    char* flag = "$[FLAG]";
    write(sockfd, flag, sizeof(flag));

    char buff[32];
    read(sockfd, buff, sizeof(buff));

    if (strncmp(buff, "OK", 2) == 0) {
        exit(0);
    }
    exit(1);
}