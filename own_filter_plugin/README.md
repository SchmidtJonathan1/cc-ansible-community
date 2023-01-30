# DoJo-Session - Own filter plugin
## Prerequisites
You just need Ansible on a node, to run the playbook.

## Task 1
Create a ansible config file with some parameters:

    1. STDOUT callback in YAML format
    2. Paths in which Ansible will search for Jinja2 Filter Plugins

Write a simple playbook with some vars to use your filter plugin and two debug tasks.

    1. Vars for example:
            unsorted_ip_list:
                - "192.168.10.1"
                ...
            unsorted_letter_list:
                - "DEV01.bar.foo"
                ...
    2. Task to use the IP filter plugin
    3. Task to use your own created Letter filter plugin


## Tasks 2
Add a second function, called sort_letter, to your python code.

```python
from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError
from ansible.module_utils.common.text.converters import to_native, to_text 

import types

## Füge die Abhänigkeiten hinzu
try:
    import netaddr
except ImportError as e:
    raise AnsibleError('Missing dependency! - %s' % to_native(e))

def sort_ip(unsorted_ip_list): 
# Function sorts a given list of IP addresses
    if not isinstance(unsorted_ip_list, list):
        raise AnsibleError("Filter needs list input, got '%s'" % type(unsorted_ip_list))
    else:
        sorted_ip_list = sorted(unsorted_ip_list, key=netaddr.IPAddress)
    return sorted_ip_list

class FilterModule(object):

    def filters(self):
        return {
            # Sorting list of IP Addresses
            'sort_ip': sort_ip
        }
```
Safe the python code to the right filter plungin folder in your ansible folder structur.


## Task 3 (Bonus)
Create a collection and add your python script. Run the playbook without any errors. 

Little hint add a new parameter inside of your ansible.cfg for

    1. Paths in which Ansible will search for collections content

## Result

If the filter plugin is written correctly, it shows the following output:

```bash
TASK [IP filter plugin] ****************************************************************************************************************************************************
task path: ./projekte/ansible/cc-ansible-community-dev/main.yml:16
Loading collection computacenter.utils from ./projekte/ansible/cc-ansible-community-dev/collections/ansible_collections/computacenter/utils
ok: [localhost] => 
  msg:
  - 192.168.10.1
  - 192.168.10.2
  - 192.168.10.4
  - 192.168.12.1

TASK [Letter filter plugin] ************************************************************************************************************************************************
task path: ./projekte/ansible/cc-ansible-community-dev/main.yml:19
Loading collection computacenter.utils from ./projekte/ansible/cc-ansible-community-dev/collections/ansible_collections/computacenter/utils
ok: [localhost] => 
  msg:
  - DEV01.la.la
  - DEV02.la.la
  - PROD01.la.la
  - QSA01.la.la

PLAY RECAP *****************************************************************************************************************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0 
```