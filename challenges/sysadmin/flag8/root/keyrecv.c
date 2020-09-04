#include <fcntl.h>
#include <unistd.h>
#include <netdb.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h>

#define SA struct sockaddr 

int main() {
    int sockfd, connfd, len; 
    struct sockaddr_in servaddr, cli; 

    sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    if (sockfd == -1) { 
        printf("socket creation failed...\n"); 
        exit(1); 
    }

    servaddr.sin_family = AF_INET; 
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(1337);

    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) { 
        printf("socket bind failed...\n"); 
        exit(1); 
    }

    if ((listen(sockfd, 5)) != 0) { 
        printf("Listen failed...\n"); 
        exit(1); 
    }

    len = sizeof(cli); 

    int fd;
    fd = open("/dev/null", O_RDWR);

    for (;;) {
        char buff[32];
        connfd = accept(sockfd, (SA*)&cli, &len);
        if (connfd < 0) { 
            printf("server accept failed...\n"); 
            exit(1); 
        }

        read(connfd, buff, sizeof(buff));
        write(fd, buff, sizeof(buff));
        if (strncmp(buff, "FLAG", 4) == 0) {
            write(connfd, "OK", 2);
        } else {
            write(connfd, "NO", 2);
        }

        close(connfd);
    }

    close(fd);
}