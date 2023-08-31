from mininet.topo import Topo

class MyTopo(Topo):
    "Ejemplo de topología simple."
    def __init__(self, num_hosts, num_switches, host_switch_links, switch_switch_links):
        # Inicializa la topología
        Topo.__init__(self)

        hosts = []
        switches = []

        # Agrega hosts
        for i in range(num_hosts):
            host = self.addHost('h{}'.format(i + 1))
            hosts.append(host)

        # Agrega switches
        for i in range(num_switches):
            switch = self.addSwitch('s{}'.format(i))
            switches.append(switch)

        # Agrega enlaces entre hosts y switches
        for link in host_switch_links:
            host_idx, switch_idx = link
            self.addLink(hosts[host_idx], switches[switch_idx])

        # Agrega enlaces entre switches
        for link in switch_switch_links:
            switch_idx1, switch_idx2 = link
            self.addLink(switches[switch_idx1], switches[switch_idx2])

def main():
    num_hosts = int(input("Ingresa el número de hosts: "))
    num_switches = int(input("Ingresa el número de switches: "))

    host_switch_links = []
    switch_switch_links = []

    for i in range(num_hosts):
        host_idx = i
        switch_idx = int(input("Ingresa el índice del switch para el host {}: ".format(i + 1)))
        host_switch_links.append((host_idx, switch_idx))

    for i in range(num_switches - 1):
        switch_idx1 = i
        switch_idx2 = i + 1
        switch_switch_links.append((switch_idx1, switch_idx2))

    for i in range(num_switches):
        for j in range(i + 1, num_switches):
            choice = input("¿Quieres conectar el switch {} con el switch {}? (s/n): ".format(i, j))
            if choice.lower() == 's':
                switch_switch_links.append((i, j))

    topo = MyTopo(
        num_hosts=num_hosts,
        num_switches=num_switches,
        host_switch_links=host_switch_links,
        switch_switch_links=switch_switch_links
    )

    # ... (Resto de tu código de configuración de Mininet) ...

if __name__ == '__main__':
    main()
