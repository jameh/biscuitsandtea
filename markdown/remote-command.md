%%%
#Program to send commands to ttys remotely
(over ssh)

##Motivation:
I was looking for a way to start up an X server on the media box without getting up off my local computer. My housemate, [@uniphil](https://github.com/uniphil "His GitHub page") came across this program on another site, which I will link to when I find it again.
%%%

##The code:
Download the C program [here]({{ url_for('media', filename='remote_command.c') }}){: download="remote_command.c" title="remote_command.c"}


```C
...

int main (int argc, char *argv[]) {
    char *cmd, *nl = "\n";
    int i, fd;
    int devno, commandno, newline;
    int mem_len;
    devno = 1; commandno = 2; newline = 0;
    if (argc < 3) {
        print_help(argv[0]);
    }
    if (argc > 3 && argv[1][0] == '-' && argv[1][1] == 'n') {
        devno = 2; commandno = 3; newline=1;
    } else if (argc > 3 && argv[1][0] == '-' && argv[1][1] != 'n') {
        printf("Invalid Option\n");
        print_help(argv[0]);
    }
    fd = open(argv[devno],O_RDWR);
    if(fd == -1) {
        perror("open DEVICE");
        exit(1);
    }
    mem_len = 0;
    for ( i = commandno; i < argc; i++ ) {
        mem_len += strlen(argv[i]) + 2;
        if ( i > commandno ) {
            cmd = (char *)realloc((void *)cmd, mem_len);
        } else { //i == commandno
            cmd = (char *)malloc(mem_len);
        }

        strcat(cmd, argv[i]);
        strcat(cmd, " ");
    }
    if (newline == 0)
        usleep(225000);
    for (i = 0; cmd[i]; i++)
        ioctl (fd, TIOCSTI, cmd+i);
    if (newline == 1)
        ioctl (fd, TIOCSTI, nl);
    close(fd);
    free((void *)cmd);
    exit (0);
}
```

##Usage
On your remote machine, compile using gcc to somewhere in your `PATH`:
```bash
gcc remote_command.c -o /usr/local/bin/remote_command
```

Then from your local device, connect via ssh:
```bash
ssh jamie@mediabox
```

and over the ssh connection, issue the command you wish to be executed on the tty of your choosing:
```bash
for i in {1..5}
do
    remote_command -n /dev/tty1 echo Hello, tty$i!
done
```

##Simplified Usage

If you are just running commands remotely, and can assume they are always to be run on `/dev/tty1`, you can simplify the process a bit with the following script:

`/usr/local/bin/remote` (or somewhere on your path):
```bash
#!/bin/bash

TTY=/dev/tty1

echo sending $@ to $TTY

sudo run_command -n $TTY $@
```

don't forget to `chmod +x /usr/local/bin/remote`, and then you can simply run commands like

```bash
remote startx
```
