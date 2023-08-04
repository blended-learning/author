import docker
import socket
from pprint import pprint
import re

hostname = socket.gethostname()

def get_public_port(local_port):
    local_port = int(local_port)
    if hostname.startswith('gpu03'):
        return local_port
    else:
        return local_port + 2001

def get_row(info):
    row = []
    image = info['Config']['Image']
    name = info['Name'].strip('/')
    row.append(name)
    row.append(image)

    # get mounts
    data_path = ""
    mounts = info['Mounts']
    for mount in mounts:
        if mount['Destination'] == '/home':
            match = re.match(r'.*/deploy/(.*)', mount['Source'])
            if match:
                data_path = match.group(1)
                break
    row.append(data_path)

    # get ports
    port_bindings = info['HostConfig']['PortBindings']
    ssh_port = None
    jupyter_port = None
    other_ports = []
    for container_port, bindings in port_bindings.items():
        local_port = bindings[0]['HostPort']
        container_port = int(container_port.replace('/tcp', ''))
        public_port = get_public_port(local_port)
        if container_port == 22:
            ssh_port = public_port
        elif container_port == 8000:
            jupyter_port = public_port
        else:
            other_ports.append((public_port, container_port))

    row.append(f'ssh :{ssh_port}' if ssh_port else '')
    row.append(f'lab :{jupyter_port}' if jupyter_port else '')
    exposed = ', '.join(f"{x}->{y}" for (x,y) in other_ports)
    row.append(f'exposed: {exposed}' if other_ports else '')

    # get gpus
    gpus = []
    try:
        for device in info['HostConfig']['DeviceRequests']:
            for caps in device['Capabilities']:
                if 'gpu' in caps:
                    gpus.extend(device['DeviceIDs'])
    except:
        pass
    gpu_message = ', '.join(sorted(gpus))
    row.append(f'GPUS: {gpu_message}' if gpus else '')
   
    return row

client = docker.DockerClient()

rows = []
for container in client.containers.list():
    info = container.attrs
    try:
        row = get_row(info)
        if row:
            rows.append(row)
    except Exception as e:
        raise(e)

from rich.console import Console
from rich.table import Table

table = Table('Research dockers')
for row in rows:
    table.add_row(*row)

console = Console()
console.print(table)
