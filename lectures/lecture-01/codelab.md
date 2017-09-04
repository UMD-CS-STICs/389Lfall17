# Codelab 1: Python 101

### Due Date

This codelab is due on *Sunday, September 10th at 11:59:59PM*. Future codelabs will be due on the Thursday before class.

### Goal

In this codelab, you'll learn (or review!) the basics of Python. We will be using Python throughout this class to build projects with AWS. Starting with next week's codelab, we will also be using the [boto3](https://github.com/boto/boto3) library, which is the official AWS SDK for Python.

### Getting Started

#### Vagrant

We will be using Vagrant, a tool for managing virtual machines via a CLI,  in this class in order to create lightweight, reproducible, and portable development environments.

##### Installation

To get started, you will need to install Virtualbox and Vagrant. If you are on Mac, you can do the installation with `brew` (see [below](#macos)). Otherwise, install Virtualbox from [here](https://www.virtualbox.org/wiki/Downloads) and Vagrant from [here](https://www.vagrantup.com/downloads.html).

Verify that the installation succeeded:

	$ vagrant version
	Installed Version: 1.9.8
	Latest Version: 1.9.8

	You're running an up-to-date version of Vagrant!
	$ virtualbox --help
	Oracle VM VirtualBox Manager 5.1.26
	(C) 2005-2017 Oracle Corporation
	All rights reserved.
	...

Now, let's test that you can successfully create a virtual machine (also called a "box") with Vagrant. Create a Vagrant box and launch it:

	$ vagrant init ubuntu/trusty64
	$ vagrant up
	$ vagrant ssh

The `init` step will auto-generate a `Vagrantfile` for you. This file specifies all of the configuration for your virtual machine. If you look at it now, you will see that it only specifies which type of virtual machine to install. In this case, we are creating a virtual machine that is running 64-bit Ubuntu Linux 14.04 (also known as "trusty").

If you've gotten this far, then everything works. Go ahead and shut down this virtual machine by running the following command:

	$ vagrant halt

Even though your VM has been halted, it is still stored on your computer. If you would like to completely remove the VM, then run this command:

	$ vagrant destroy

###### macOS

First, install [`brew`](https://brew.sh/) if you do not already have it on your system:

	$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Now, use `brew cask` to install `Virtualbox` and `Vagrant`:

	$ brew cask install virtualbox
	$ brew cask install vagrant

Continue with the installation instructions from above, starting at the installation verification.

#### Codelab Vagrant Environment

For this codelab, I will be providing you with a `Vagrantfile` that specifies all of the configuration.

First, clone the [class repository](https://github.com/UMD-CS-STICs/389Lfall17) onto your system:

	$ git clone https://github.com/UMD-CS-STICs/389Lfall17.git

Each week, when new content is pushed into this repository, you'll need to pull in these changes. All you need to do is run:

	$ git pull

This is a good time to remind you to not share any of your solutions to these codelabs or projects. However, when you start on the final project, you are welcome to share that on GitHub or elsewhere.

### Learn Python in Y Minutes

Since you are already familiar with Ruby from CMSC330, then you mostly just need to learn the syntactical differences. For that, I ask that you go through the "Learn X in Y Minutes" tutorial for Python 3 here:

https://learnxinyminutes.com/docs/python3/

### More on Python (Optional)

If you would like to take a deeper dive into the internals of Python, I would recommend checking out the following resources (read: skimming the parts that interest you!):

[Python Library Reference](https://docs.python.org/3/library/index.html)
[Python Language Reference](https://docs.python.org/3/reference/index.html)

### Assignment

To give your new Python knowledge a test drive, you're going to write a few simple functions.

Open the folder `lectures/lecture-01/codelab/`. Go ahead and open `functions.py` and `test.py` in your editor. `functions.py` contains the three functions that you will need to implement, and `test.py` contains the public tests that you should pass in order to get full credit. 

1. `foobar_flip(value)`
2. `string_compress(string)`
3. `fibonacci(n)`

Note that to pass the the final public test (`test_large_numbers`), you will need to write your fibonacci method using a Python dictionary. If you don't solve this function, you'll still get full credit.

To run this codelab, you will need to launch the Vagrant environment. It comes pre-configured with our Python environment.

	$ # /lectures/lecture-01/codelab
	$ vagrant up
	$ vagrant ssh
	vagrant$ cd code

Now run the tests:

	vagrant$ python tests.py

Now implement the functions. You can implement them one at a time, as all of the test cases will execute independently.

You'll see a message like this when you've passed all of them:

	$ python test.py
	........
	----------------------------------------------------------------------
	Ran 8 tests in 0.002s

	OK
