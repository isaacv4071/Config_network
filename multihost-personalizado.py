from mininet.topo import Topo

class MyTopo(Topo):
    "Simple topology example."
    def __init__(self, num_hosts, num_switches):
        "Create custom topo."
        # Initialize topology
        Topo.__init__(self)

        hosts = []
        switches = []

        # Add hosts
        for i in range(num_hosts):
            host = self.addHost('h{}'.format(i))
            hosts.append(host)

        # Add switches
        for i in range(num_switches):
            switch = self.addSwitch('s{}'.format(i))
            switches.append(switch)

        # Add links
        for i, host in enumerate(hosts):
            self.addLink(host, switches[i % num_switches])

        for i in range(num_switches - 1):
            self.addLink(switches[i], switches[i + 1])

topos = {'mytopo': (lambda num_hosts, num_switches: MyTopo(num_hosts, num_switches))}
