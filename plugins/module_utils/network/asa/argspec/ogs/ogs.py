#
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
The arg spec for the asa_ogs module
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class OGsArgs(object):
    """The arg spec for the asa_ogs module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "elements": "dict",
            "type": "list",
            "options": {
                "object_type": {
                    "type": "str",
                    "required": True,
                    "choices": [
                        "icmp-type",
                        "network",
                        "protocol",
                        "security",
                        "service",
                        "user",
                    ],
                },
                "object_groups": {
                    "elements": "dict",
                    "type": "list",
                    "options": {
                        "name": {"required": True, "type": "str"},
                        "description": {"type": "str"},
                        "icmp_type": {
                            "type": "dict",
                            "options": {
                                "icmp_object": {
                                    "type": "list",
                                    "choices": [
                                        "alternate-address",
                                        "conversion-error",
                                        "echo",
                                        "echo-reply",
                                        "information-reply",
                                        "information-request",
                                        "mask-reply",
                                        "mask-request",
                                        "mobile-redirect",
                                        "parameter-problem",
                                        "redirect",
                                        "router-advertisement",
                                        "router-solicitation",
                                        "source-quench",
                                        "time-exceeded",
                                        "timestamp-reply",
                                        "timestamp-request",
                                        "traceroute",
                                        "unreachable",
                                    ],
                                }
                            },
                        },
                        "network_object": {
                            "type": "dict",
                            "options": {
                                "host": {"type": "list"},
                                "address": {"type": "list"},
                                "ipv6_address": {"type": "list"},
                                "object": {"type": "str"},
                            },
                        },
                        "protocol_object": {
                            "type": "dict",
                            "options": {
                                "protocol": {
                                    "type": "list",
                                    "choices": [
                                        "ah",
                                        "eigrp",
                                        "esp",
                                        "gre",
                                        "icmp",
                                        "icmp6",
                                        "igmp",
                                        "igrp",
                                        "ip",
                                        "ipinip",
                                        "ipsec",
                                        "nos",
                                        "ospf",
                                        "pcp",
                                        "pim",
                                        "pptp",
                                        "sctp",
                                        "snp",
                                        "tcp",
                                        "udp",
                                    ],
                                }
                            },
                        },
                        "security_group": {
                            "type": "dict",
                            "options": {
                                "sec_name": {"type": "list"},
                                "tag": {"type": "list"},
                            },
                        },
                        "service_object": {
                            "type": "dict",
                            "options": {
                                "protocol": {
                                    "type": "list",
                                    "choices": [
                                        "ah",
                                        "eigrp",
                                        "esp",
                                        "gre",
                                        "icmp",
                                        "icmp6",
                                        "igmp",
                                        "igrp",
                                        "ip",
                                        "ipinip",
                                        "ipsec",
                                        "nos",
                                        "ospf",
                                        "pcp",
                                        "pim",
                                        "pptp",
                                        "sctp",
                                        "snp",
                                        "tcp",
                                        "tcp-udp",
                                        "udp",
                                    ],
                                },
                                "object": {"type": "str"},
                            },
                        },
                        "user_object": {
                            "type": "dict",
                            "options": {
                                "user": {
                                    "elements": "dict",
                                    "type": "list",
                                    "options": {
                                        "name": {
                                            "required": True,
                                            "type": "str",
                                        },
                                        "domain": {
                                            "required": True,
                                            "type": "str",
                                        },
                                    },
                                },
                                "user_group": {
                                    "elements": "dict",
                                    "type": "list",
                                    "options": {
                                        "name": {
                                            "required": True,
                                            "type": "str",
                                        },
                                        "domain": {
                                            "required": True,
                                            "type": "str",
                                        },
                                    },
                                },
                            },
                        },
                        "group_object": {"type": "str"},
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }
