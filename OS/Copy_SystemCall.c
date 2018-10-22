#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

void file_copy(int f1,int f2);

int main(int argc, char *argv[]) {
	if(argc != 3) {
	printf("\nFile Not Found");
	exit (0); }
	
	int fd1=open(argv[1],0);
	if(fd1==-1) {
	printf("\nError in File Opening");
	exit(1);
	}
	
	int fd2=creat(argv[2],066);
	if(fd2==-1){
	printf("\nError While Creating File");
	exit (0);
	}
	
	file_copy(fd1,fd2);
	close(fd1);
	close(fd2);
	return 0;
}

void file_copy(int f1,int f2) {
	char buf[512];
	int cnt;
	while(cnt=read(f1,buf,sizeof(buf))) write(f2,buf,cnt);
}
