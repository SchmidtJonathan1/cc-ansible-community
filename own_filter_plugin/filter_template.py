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
