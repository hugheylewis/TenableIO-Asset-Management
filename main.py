from time import strftime, localtime
from tenable.io import TenableIO
from config.config import APIkeys


tio = TenableIO(APIkeys.accessKey,
                APIkeys.secretKey, vendor='',  # edit required
                product='Tenable Asset Management', build='1.0.0')


def convert_to_localtime(epoch):
    local_time = strftime('%Y-%m-%d', localtime(epoch))
    return local_time


def get_assets():
    total = 0
    total_with_scan_times = 0
    old_agents = []
    for agent in tio.agents.list():
        if 'last_scanned' in agent:
            print(f"{agent['name']}: {convert_to_localtime(agent['last_scanned'])}: {agent['id']}")
            total_with_scan_times += 1
        total += 1
    print(f"Total number of agents: {total}")
    print(f"Total number of agents with valid scan time: {total_with_scan_times}")

    # TODO: Append old agents to the `old_agents` list


get_assets()

