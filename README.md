# ZyxelFWUnpacker
Set of scripts for automatic extraction of Zyxer firmware upgrades.

Usage
-----
1. Create LoAL
2. Launch *./onefile.sh* with first argument as ROM file, and second as LoAL file. Additionally you can add output file as third argument.
3. After one long file created it can be split by *./splitfiles.py*, where you specify your extracted file as a first argument.

Your files will be extracted into ./files/ directory.

Creating LoAL - list of addresses and lengths
------------------------------------
First, you need to identify addresses and lengths for archive, I used binwalk for that:
```
$ binwalk V1.00\(AARP.9\)C0.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
64            0x40            LZMA comp... 32754 bytes
5953          0x1741          LZMA comp... 32751 bytes
...			  0x...			  LZMA comp... ..... bytes
...			  0x...			  LZMA comp... ..... bytes
456940        0x6F8EC         LZMA comp... 32761 bytes
463281        0x711B1         LZMA comp... 14040 bytes

```

Now, you have to write all of them into bash array.

I used sublime to quickly create file like this:

```bash
countto=66
address=(64 5953 ... ... 456940 463281)
length=(32754 32751 ... ... 32761 14040)
```


**countto** - determines how many blocks there are in ROM, because ROM consists of multiple compressed files with size of about 32kb

**address** - array of addresses IN DECIMAL (first column in binwalk)

**length** - array of lengths for each archive.


But if you dislike or find it too frustrating to do this way you can do it like this:
```bash
countto=66
address[0]=64
length[0]=32754
address[1]=5953
length[1]=32751
address[...]=...
length[...]=...
address[64]=456940
length[64]=32761
address[65]=463281
length[65]=14040
```

TODO
----
* Packer
* Automatic LoAL creator