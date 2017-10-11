# Vagrant Boxes

In this class, we will use Vagrant to manage a virtual environment in which we will work on codelabs and projects. This gives us a recreatable environment running the same OS (Ubuntu 16.04) as that which we will use on EC2. It also creates an environment that is set

The folder `vagrant` in the root directory of this repo contains all codelabs, projects and Vagrant-related configuration.

The `Vagrantfile` configures your box with a variety of tools to improve your development experience, including:
- Shell command syntax highlighting
- AWS CLI auto-completion
- AWS credentials
- Python 3.6.2
- AWS pre-configured with the `us-east-1` region

Using a vagrant box also makes it easier for you to experiment without screwing up your developer environment (installing global python packages, overwriting your host's default Python, etc.). In the worst case, you can simply destroy your Vagrant box and re-provision it.

All files stored in the shared directories (`codelabs`, `keys`, `projects`) are persisted even if you destroy your Vagrant box. All other files will be lost -- so be careful.

## AWS Credentials

You will need to store your AWS credentials in a file, `aws.credentials`, in the root directory of this repo. Look for `aws.credentials.example`. Copy and rename this file, then insert your AWS credentials (access key id and secret access key).

This file should look like this (except with your credentials):
```
[default]
aws_access_key_id = AIUBG23BWONGOIWEN83N
aws_secret_access_key = oinwgoi2n3th040BIGUEBW4t8h493g3nUUB023jn
```

Also, these are fake credentials. Don't ever share your AWS credentials, else before you know it you will have cryptocurrency miners running and you'll be footing the bill. Don't be like [these folks](https://github.com/search?utf8=%E2%9C%93&q=remove+aws+credentials&type=Commits) and never commit this file (it is in our `.gitignore`). If you ever do this, then 1) immediately disable those credentials and 2) remove that commit from your git history.

## EC2 Key Pairs

As we work with EC2, you will want to place all EC2 key pairs into the `vagrant/keys` directory. These key pairs will be shared with your Vagrant environment.

## Useful Commands

Launch a Vagrant box:

```
$ vagrant up
```

SSH onto a Vagrant box:

```
$ vagrant ssh
```

Shut down a Vagrant box:

```
$ vagrant halt
```

Destroy a Vagrant box:

```
$ vagrant destroy
```
