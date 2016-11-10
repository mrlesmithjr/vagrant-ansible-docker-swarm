#! /usr/bin/env python

# docker_hostname = '192.168.202.200'
# docker_port = '2377'
# docker_protocol = 'tcp'

import argparse
import json
from docker import Client
#cli = Client(base_url=docker_protocol+'://'+docker_hostname+':'+docker_port)
cli = Client(base_url='unix://var/run/docker.sock')

class DOCKERMGMT(object):
    def __init__(self):
        self.read_cli_args()
        self.decide_action()

    def decide_action(self):
        if self.args.action == 'containers':
            self.docker_containers()
        if self.args.action == 'info':
            self.docker_info()
        if self.args.action == 'images':
            self.docker_images()
        if self.args.action == "inspect_node":
            self.docker_inspect_node()
        if self.args.action == 'networks':
            self.docker_networks()
        if self.args.action == "nodes":
            self.docker_nodes()
        if self.args.action == "services":
            self.docker_services()

    def docker_containers(self):
        dc = cli.containers()
        print json.dumps(dc, indent=4)

    def docker_images(self):
        dimg = cli.images()
        print json.dumps(dimg, indent=4)

    def docker_info(self):
        di = cli.info()
        print json.dumps(di, indent=4)

    def docker_inspect_node(self):
        dis = cli.inspect_node(self.args.node)
        print json.dumps(dis, indent=4)

    def docker_networks(self):
        dnets = cli.networks()
        print json.dumps(dnets, indent=4)

    def docker_nodes(self):
        if self.args.role is None:
            if self.args.node is None:
                dn = cli.nodes()
            elif self.args.node is not None:
                dn = cli.nodes(filters={'name': self.args.node})
        elif self.args.role is not None:
            if self.args.node is None:
                dn = cli.nodes(filters={'role': self.args.role})
            elif self.args.node is not None:
                dn = cli.nodes(filters={'role': self.args.role, 'name': self.args.node})
        print json.dumps(dn, indent=4)

    def docker_services(self):
        if self.args.name is None:
            svcs = cli.services()
        elif self.args.name is not None:
            svcs = cli.services(filters={'name': self.args.name})
        print json.dumps(svcs, indent=4)

    def read_cli_args(self):
        parser = argparse.ArgumentParser(description='Docker Management')
        parser.add_argument('action', help='Define action to take',
                           choices=['containers', 'info', 'images', 'inspect_node', 'networks', 'nodes', 'services'])
        parser.add_argument('--name', help='Define name to use as filter')
        parser.add_argument('--node', help='Define node to inspect')
        parser.add_argument('--role', choices=['manager', 'worker'])
        self.args = parser.parse_args()

if __name__ == '__main__':
    DOCKERMGMT()
