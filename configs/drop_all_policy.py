"""Default drop Zorp policy"""

from  Zorp.Core import *


def default_instance():
    """
    Declares only one rule that matches all the traffic and
    refers to a services that denies all the traffic.
    """

    DenyService(name='DenyService',
                ipv4_setting=DenyIPv4.DROP,
                ipv6_setting=DenyIPv6.DROP
    )

    Rule(service='DenyService'
    )
