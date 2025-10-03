Hex is represented by 0xYY where each Y is a hex digit that ranges from 0 (A) - 15 (F). So each Y can be represented with 4 bits where 0000 means 0 and 1111 means 15. Therefore two digits (two YYs in 0xYY)in a hex digit
are represented by two 4 bits OR 8 bits in total --> which equals 1 byte in total. Also the 0x prefix is used to represent hex

0xAC --> 1010 1100 --> 8 bits = 1 byte

if you see something like 0xYYYY ---> need 4*4 bits to represent (since each digit is 4 bits and there are four of them in total)--> like 1111 1111 1111 1111 

When calculating checksums of payloads -> consider each block of data as made up of 4 hex digits --> 0xYYYY