<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Purpose](#purpose)
  - [Requirements](#requirements)
  - [Information](#information)
  - [Usage](#usage)
  - [License](#license)
  - [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Purpose

Spins up a [Docker](https://www.docker.com) Swarm mode cluster within a
[Vagrant](https://www.vagrantup.com) environment and uses
[Ansible](https://www.ansible.com) to provision the whole environment.

## Requirements

-   [Ansible](https://www.ansible.com)
-   [VirtualBox](https://www.virtualbox.org)
-   [Vagrant](https://www.vagrantup.com)

## Information

This environment will consist of the following:

-   7 [Ubuntu](https://www.ubuntu.com) `16.04` nodes
    -   3 [Docker](https://www.docker.com) Swarm Managers (node0-node2)
    -   4 [Docker](https://www.docker.com) Swarm Workers (node3-node6)

I have also included a [Python] script `docker-management.py` that will be
worked on over time to do some initial various things but will have more
functionality over time.

## Usage

Easily spin up the [Vagrant](https://www.vagrantup.com) environment.

```bash
vagrant up
```

Once everything provisions you are now ready to begin using your [Docker](https://www.docker.com) Swarm
mode cluster.

Connect to one of the [Docker](https://www.docker.com) Swarm Managers to begin creating services and etc.

```bash
vagrant ssh node0
```

Validate that the [Docker](https://www.docker.com) Swarm cluster is functional:

```bash
sudo docker node ls
```

You should something similar to below:

```bash
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
0bp91mlgswsl19chkudasptxt    node3     Ready   Active
0uyl5ms4lb543d6284vrycuh1    node5     Ready   Active
1trucugnb1gmu35tmjt4jc2om    node4     Ready   Active
4y83hx5ywpkn65tp268huipyz *  node0     Ready   Active        Leader
5suz75nggempf5984cx99e6sx    node6     Ready   Active
60qm8mohj517vovv7id5p7l6s    node2     Ready   Active        Reachable
cwnkijv7f8gzsvwltnomgmmea    node1     Ready   Active        Reachable
```

Create a new [Docker](https://www.docker.com) service:

```bash
sudo docker service create --name web --publish 8080:80 --replicas 1 mrlesmithjr/nginx
```

List the current [Docker](https://www.docker.com) services:

```bash
sudo docker service ls
...
ID            NAME  REPLICAS  IMAGE              COMMAND
016psrb2tb7y  web   1/1       mrlesmithjr/nginx
```

List the tasks of a service:

```bash
sudo docker service ps web
...
ID                         NAME   IMAGE              NODE   DESIRED STATE  CURRENT STATE               ERROR
9n3yq6k2ig71kkldzrs2zfqb3  web.1  mrlesmithjr/nginx  node0  Running        Running about a minute ago
```

Scale the service to increase the number of replicas:

```bash
sudo docker service scale web=4
...
web scaled to 4
```

Now list the current [Docker](https://www.docker.com) services:

```bash
sudo docker service ls
...
ID            NAME  REPLICAS  IMAGE              COMMAND
016psrb2tb7y  web   4/4       mrlesmithjr/nginx
```

Now list the tasks of the service:

```bash
sudo docker service ps web
...
ID                         NAME   IMAGE              NODE   DESIRED STATE  CURRENT STATE           ERROR
9n3yq6k2ig71kkldzrs2zfqb3  web.1  mrlesmithjr/nginx  node0  Running        Running 5 minutes ago
bisd4qcaxsx66u6zeuomykkr3  web.2  mrlesmithjr/nginx  node3  Running        Running 41 seconds ago
8u940el4iomekvsfkqvpz75ox  web.3  mrlesmithjr/nginx  node4  Running        Running 43 seconds ago
dhjjumf7auf6s5k8uqwjo6wbx  web.4  mrlesmithjr/nginx  node1  Running        Running 40 seconds ago
```

Now go and enjoy your [Docker](https://www.docker.com) Swarm mode cluster and do some learning.

## License

BSD

## Author Information

Larry Smith Jr.

-   [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
-   [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
-   [mrlesmithjr](http://mrlesmithjr.com)
-   mrlesmithjr [at] gmail.com
