# y-datecount
A command line calculator for dates.

## Motivation
Sometimes I would find myself searching the web to find an online tool to see how many days were passed since my anniversary, or what date it is 100 days later.
So the idea of using an offline date calculator emerged.

## Features
* Calculate the number of days since/until a specified date.
* Calculate the number of days between two specified dates.
* Show the date of x days ago/later specified by user.
* Show the date of x days before/after a date specified by user.

## Supported Platforms

* Linux (tested on Ubuntu 20.04 LTS)
* macOS (coming soon)

## Installation

### Install from Binary

Go to the "releases" tab and download the latest binary release.

Run the programme from the command line.

```sh
cd /path/to/downloaded/file && chmod +x ydatecount && ./ydatecount
```

where `/path/to/downloaded/file` is the location where the downloaded binary is.

### Build from Source

#### Option 1

Clone the source and change directory.

```sh
$ git clone https://github.com/Badboy-16/y-datecount && cd y-datecount 
```

Run `build.py`.

`build.py` will install the dependency and build the binary.

```sh
python3 build.py 
```

Run the programme.

```sh
./ydatecount 
```

#### Option 2

Clone the source and change directory.

```sh
$ git clone https://github.com/Badboy-16/y-datecount && cd y-datecount 
```

Install dependency.

```sh
$ pip3 install pyinstaller 
```

Build the programme.

```sh
$ pyinstaller -F -n ydatecount __main__.py 
```

Run the programme.

```sh
$ cd dist && chmod +x ydatecount && ./ydatecount 
```

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

