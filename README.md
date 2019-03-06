<img src="https://www.holbertonschool.com/holberton-logo-twitter-card.png">

# Low-level programming - C
Low-level programming & Algorithm

## Contents
* [Purpose](https://github.com/sumin3/holbertonschool-low_level_programming#Purpose)
* [Coding style](https://github.com/sumin3/holbertonschool-low_level_programming#Coding-style)
* [Usage](https://github.com/sumin3/holbertonschool-low_level_programming#usage)
* [Installation](https://github.com/sumin3/holbertonschool-low_level_programming#installation)
* [Usage Example](https://github.com/sumin3/holbertonschool-low_level_programming#Usage-Example)
* [Author](https://github.com/sumin3/holbertonschool-low_level_programming#author)


## Purpose
This repository contains projects for training C programming. All projects are in C and are designed to learn C from beginning level to advanced level. All projects can seperate into three parts
1. Hatching out (directory from 0x00 to 0x09, from 0x0A to 0xF, 0x10, and 0x13)
2. Data structures and Algorithms (directory 0x11 and 0x12)
3. Linux and Unix system programming (directory 0x14 and 0x15)

## Coding style
- All C files are compiled on Ubuntu 14.04 LTS and using [Betty Style](https://\github.com/holbertonschool/Betty) for checking coding and documentation styles. In most of project, standard library function is not allow to use, except `malloc`, `free`, and `exit`.

## Installation
To use, first download  this repository into your local machine by issuing the following command in your local terminal.
```
git clone https://github.com/sumin3/holbertonschool-low_level_programming.git
```
#### Directory
Each directoy's name includes information below
1. a number which orders projects from beginning to advanced level
2. name of programming language
3. concept/topic.
#### Change Directory
```
cd <directory name>
```
After change current working directory, issue the following command to compile \
the code

## Usage
```
gcc -Wall -Werror -Wextra -pedantic <filename.c> -o <output filename>
```
Once the .c files are compiled you can run the program by issuing the command
```
./<output filename>
```

### Usage Example
```
$ gcc -Wall -pedantic -Werror -Wextra 1-main.c 1-isdigit.c -o 1-isdigit
$ ./1-isdigit
0: 1
a: 0
```

## Author
Leine Valente - [Twitter: @LeineFran](https://twitter.com/LeineFran)