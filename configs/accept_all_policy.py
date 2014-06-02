"""Default accept Zorp policy"""

from  Zorp.Core import *


def default_instance():
    """
    Declares only one rule that matches all the traffic and
    refers to a services that forwards all the traffic transparently.
    """

    PFService(name='PFService'
              router=TransparentRouter(),
    )

    Rule(service='PFService'
    )
