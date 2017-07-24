#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(){
	int status = system("kill $(./ps aux | grep './eog' | awk '{print $2}')");
}
