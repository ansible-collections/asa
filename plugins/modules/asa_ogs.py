#!/usr/bin/python
# pylint: skip-file
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for asa_ogs
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: asa_ogs
short_description: Object Group resource module
description: This module configures and manages Objects and Groups on ASA platforms.
version_added: 1.0.0
author: Sumit Jaiswal (@justjais)
notes:
- Tested against Cisco ASA Version 9.10(1)11
- This module works with connection C(network_cli). See L(ASA Platform Options,../network/user_guide/platform_asa.html).
options:
  config:
    description: A list of Object Group options.
    type: list
    elements: dict
    suboptions:
      object_type:
        description: The object group type.
        type: str
        required: true
        choices:
        - icmp-type
        - network
        - protocol
        - security
        - service
        - user
      object_groups:
        description: The object groups.
        type: list
        elements: dict
        suboptions:
          name:
            description: Specifies object-group ID
            required: true
            type: str
          description:
            description: The description for the object-group.
            type: str
          icmp_type:
            description: Configure an ICMP-type object
            type: dict
            suboptions:
              icmp_object:
                description: Defines the ICMP types in the group.
                type: list
                choices: [alternate-address, conversion-error, echo, echo-reply, information-reply,
                  information-request, mask-reply, mask-request, mobile-redirect,
                  parameter-problem, redirect, router-advertisement, router-solicitation,
                  source-quench, time-exceeded, timestamp-reply, timestamp-request,
                  traceroute, unreachable]
          network_object:
            description: Configure a network object
            type: dict
            suboptions:
              host:
                description: Set this to specify a single host object.
                type: list
              address:
                description: Enter an IPv4 network address with space seperated netmask.
                type: list
              ipv6_address:
                description: Enter an IPv6 prefix.
                type: list
          protocol_object:
            description: Configure a protocol object
            type: dict
            suboptions:
              protocol:
                description: Defines the protocols in the group.
                type: list
                choices: [ah, eigrp, esp, gre, icmp, icmp6, igmp, igrp, ip, ipinip,
                  ipsec, nos, ospf, pcp, pim, pptp, sctp, snp, tcp, udp]
          security_group:
            description: Configure a security-group
            type: dict
            suboptions:
              sec_name:
                description: Enter this keyword to specify a security-group name.
                type: list
              tag:
                description: Enter this keyword to specify a security-group tag.
                type: list
          service_object:
            description: Configure a service object
            type: dict
            suboptions:
              protocol:
                description: Defines the protocols in the group.
                type: list
                choices: [ah, eigrp, esp, gre, icmp, icmp6, igmp, igrp, ip, ipinip,
                  ipsec, nos, ospf, pcp, pim, pptp, sctp, snp, tcp, tcp-udp, udp]
              object:
                description: Enter this keyword to specify a service object
                type: str
          user_object:
            description: Configures single user, local or import user group
            type: dict
            suboptions:
              user:
                description: Configure a user objectUser name to configure a user
                  object.
                type: list
                elements: dict
                suboptions:
                  name:
                    description: Enter the name of the user
                    type: str
                    required: true
                  domain:
                    description: User domain
                    type: str
                    required: true
              user_group:
                description: Configure a user group object.
                type: list
                elements: dict
                suboptions:
                  name:
                    description: Enter the name of the group
                    type: str
                    required: true
                  domain:
                    description: Group domain
                    type: str
                    required: true
  running_config:
    description:
    - The module, by default, will connect to the remote device and retrieve the current
      running-config to use as a base for comparing against the contents of source.
      There are times when it is not desirable to have the task get the current running-config
      for every task in a playbook.  The I(running_config) argument allows the implementer
      to pass in the configuration to use as the base config for comparison. This
      value of this option should be the output received from device by executing
      command.
    type: str
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
"""

EXAMPLES = """

# Using merged

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_network_og
#  network-object host 192.0.3.1

- name: "Merge module attributes of given object-group"
  cisco.asa.asa_ogs:
    config:
    - object_type: network
      object_groups:
        - name: test_og_network
          description: test_og_network
          network_object:
            host:
              - 192.0.2.1
              - 192.0.2.2
            address:
              - 192.0.2.0 255.255.255.0
              - 198.51.100.0 255.255.255.0
        - name: test_network_og
          description: test_network_og
          network_object:
            host:
              - 192.0.3.1
              - 192.0.3.2
            ipv6_address:
              - 2001:db8:3::/64
    - object_type: security
      object_groups:
        - name: test_og_security
          description: test_security
          security_group:
            sec_name:
              - test_1
              - test_2
            tag:
              - 10
              - 20
    - object_type: user
      object_groups:
        - name: test_og_user
          description: test_user
          user_object:
            user:
              - name: new_user_1
                domain: LOCAL
              - name: new_user_2
                domain: LOCAL
    state: merged

# Commands fired:
# ---------------
#
# object-group security test_og_security
#  description test_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group network test_og_network
#  description test_og_network
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
# object-group network test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:3::/64
# object-group user test_og_user
#  description test_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

# After state:
# ------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
#  network-object host 192.0.3.1
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  description test_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

# Using Replaced

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

- name: "Replace module attributes of given object-group"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
            description: test_og_network_replace
            network_object:
              host:
                - 192.0.3.1
              address:
                - 192.0.3.0 255.255.255.0
      - object_type: protocol
        object_groups:
          - name: test_og_protocol
            description: test_og_protocol
            protocol_object:
              protocol:
                - tcp
                - udp
    state: replaced

# Commands Fired:
# ---------------
#
# object-group protocol test_og_protocol
# description test_og_protocol
# protocol tcp
# protocol udp
# object-group network test_og_network
# description test_og_network_replace
# no network-object 192.0.2.0 255.255.255.0
# no network-object 198.51.100.0 255.255.255.0
# network-object 192.0.3.0 255.255.255.0
# no network-object host 192.0.2.1
# no network-object host 192.0.2.2
# network-object host 192.0.3.1

# After state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network_replace
#  network-object host 192.0.3.1
#  network-object 192.0.3.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2
# object-group protocol test_og_protocol
#  protocol-object tcp
#  protocol-object udp

# Using Overridden

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

- name: "Overridden module attributes of given object-group"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
            description: test_og_network_override
            network_object:
              host:
                - 192.0.3.1
              address:
                - 192.0.3.0 255.255.255.0
      - object_type: protocol
        object_groups:
          - name: test_og_protocol
            description: test_og_protocol
            protocol_object:
              protocol:
                - tcp
                - udp
    state: overridden

# Commands Fired:
# ---------------
#
# no object-group security test_og_security
# no object-group user test_og_user
# object-group protocol test_og_protocol
# description test_og_protocol
# protocol tcp
# protocol udp
# object-group network test_og_network
# description test_og_network_override
# no network-object 192.0.2.0 255.255.255.0
# no network-object 198.51.100.0 255.255.255.0
# network-object 192.0.3.0 255.255.255.0
# no network-object host 192.0.2.1
# no network-object host 192.0.2.2
# network-object host 192.0.3.1
# no object-group network test_network_og

# After state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network_override
#  network-object host 192.0.3.1
#  network-object 192.0.3.0 255.255.255.0
# object-group protocol test_og_protocol
#  protocol-object tcp
#  protocol-object udp

# Using Deleted

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

- name: "Delete given module attributes"
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
          - name: test_network_og
      - object_type: security
        object_groups:
          - name: test_og_security
    state: deleted

# Commands Fired:
# ---------------
#
# no object-group network test_og_network
# no object-group network test_network_og
# no object-group security test_og_security

# After state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

# Using DELETED without any config passed
#"(NOTE: This will delete all of configured resource module attributes)"

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

- name: Delete ALL configured module attributes
  cisco.asa.asa_ogs:
    config:
    state: deleted

# Commands Fired:
# ---------------
#
# no object-group network test_og_network
# no object-group network test_network_og
# no object-group security test_og_security
# no object-group user test_og_user

# After state:
# -------------
#
# ciscoasa# sh running-config object-group

# Using Gathered

# Before state:
# -------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

- name: Gather listed OGs with provided configurations
  cisco.asa.asa_ogs:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "object_groups": [
#                 {
#                     "description": "test_security",
#                     "name": "test_og_security",
#                     "security_group": {
#                         "sec_name": [
#                             "test_2",
#                             "test_1"
#                         ],
#                         "tag": [
#                             10,
#                             20
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "security"
#         },
#         {
#             "object_groups": [
#                 {
#                     "description": "test_network_og",
#                     "name": "test_network_og",
#                     "network_object": {
#                         "host": [
#                             "192.0.3.1",
#                             "192.0.3.2"
#                         ],
#                         "ipv6_address": [
#                             "2001:db8:3::/64"
#                         ]
#                     }
#                 },
#                 {
#                     "description": "test_og_network",
#                     "name": "test_og_network",
#                     "network_object": {
#                         "address": [
#                             "192.0.2.0 255.255.255.0",
#                             "198.51.100.0 255.255.255.0"
#                         ],
#                         "host": [
#                             "192.0.2.1",
#                             "192.0.2.2"
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "network"
#         },
#         {
#             "object_groups": [
#                 {
#                     "description": "test_user",
#                     "name": "test_og_user",
#                     "user_object": {
#                         "user": [
#                             {
#                                 "domain": "LOCAL",
#                                 "name": "new_user_1"
#                             },
#                             {
#                                 "domain": "LOCAL",
#                                 "name": "new_user_2"
#                             }
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "user"
#         }
#     ]

# After state:
# ------------
#
# ciscoasa# sh running-config object-group
# object-group network test_og_network
#  description test_og_network
#  network-object host 192.0.2.1
#  network-object host 192.0.2.2
#  network-object 192.0.2.0 255.255.255.0
#  network-object 198.51.100.0 255.255.255.0
# object-group network test_network_og
#  description test_network_og
#  network-object host 192.0.3.1
#  network-object host 192.0.3.2
#  network-object 2001:db8:0:3::/64
#  group-object test_og_network
# object-group security test_og_security
#  security-group name test_1
#  security-group name test_2
#  security-group tag 10
#  security-group tag 20
# object-group user test_og_user
#  user LOCAL\\new_user_1
#  user LOCAL\\new_user_2

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.asa.asa_ogs:
    config:
      - object_type: network
        object_groups:
          - name: test_og_network
            description: test_og_network
            network_object:
              host:
                - 192.0.2.1
                - 192.0.2.2
              address:
                - 192.0.2.0 255.255.255.0
                - 198.51.100.0 255.255.255.0
          - name: test_network_og
            description: test_network_og
            network_object:
              host:
                - 192.0.3.1
                - 192.0.3.2
              ipv6_address:
                - 2001:db8:3::/64
      - object_type: security
        object_groups:
          - name: test_og_security
            description: test_security
            security_group:
              sec_name:
                - test_1
                - test_2
              tag:
                - 10
                - 20
      - object_type: user
        object_groups:
          - name: test_og_user
            description: test_user
            user_object:
              user:
                - name: new_user_1
                  domain: LOCAL
                - name: new_user_2
                  domain: LOCAL
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "object-group security test_og_security",
#         "description test_security",
#         "security-group name test_1",
#         "security-group name test_2",
#         "security-group tag 10",
#         "security-group tag 20",
#         "object-group network test_og_network",
#         "description test_og_network",
#         "network-object 192.0.2.0 255.255.255.0",
#         "network-object 198.51.100.0 255.255.255.0",
#         "network-object host 192.0.2.1",
#         "network-object host 192.0.2.2",
#         "object-group network test_network_og",
#         "description test_network_og",
#         "network-object host 192.0.3.1",
#         "network-object host 192.0.3.2",
#         "network-object 2001:db8:3::/64",
#         "object-group user test_og_user",
#         "description test_user",
#         "user LOCAL\\new_user_1",
#         "user LOCAL\\new_user_2"
#     ]

# Using Parsed

# parsed.cfg
#
# object-group network test_og_network
#   description test_og_network
#   network-object host 192.0.2.1
#   network-object 192.0.2.0 255.255.255.0
# object-group network test_network_og
#   network-object 2001:db8:3::/64
# object-group service test_og_service
#   service-object tcp-udp

- name: Parse the commands for provided configuration
  cisco.asa.asa_ogs:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "object_groups": [
#                 {
#                     "name": "test_network_og"
#                 },
#                 {
#                     "description": "test_og_network",
#                     "name": "test_og_network",
#                     "network_object": {
#                         "host": [
#                             "192.0.2.2"
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "network"
#         },
#         {
#             "object_groups": [
#                 {
#                     "name": "test_og_service",
#                     "service_object": {
#                         "protocol": [
#                             "tcp-udp",
#                             "ipinip"
#                         ]
#                     }
#                 }
#             ],
#             "object_type": "service"
#         }
#     ]

"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['object-group network test_network_og', 'description test_network_og', 'network-object host 192.0.2.1']
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.argspec.ogs.ogs import (
    OGsArgs,
)
from ansible_collections.cisco.asa.plugins.module_utils.network.asa.config.ogs.ogs import (
    OGs,
)


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """

    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]

    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=OGsArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )
    result = OGs(module).execute_module()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
