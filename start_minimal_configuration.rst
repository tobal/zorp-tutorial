---------------------
Minimal Configuration
---------------------

The main problem of transparent proxy firewalls is the fact that the traffic does not target the firewall itself, but a host behind the network security device. In a usual case the traffic is forwarded to the originally targeted server, but in case of a firewall the traffic must be delivered locally to the proxy, which will connect to the originally targeted server, or another according to the policy. The divertable packets should be identified somehow in the packet filter rulesets. It can be performed by the means of transparent proxy (`TProxy <http://www.balabit.com/support/community/products/tproxy>`_) kernel module of the kernel.

  The idea is to identify packets with the destination address matching a local socket on your box, set the packet mark to a certain value, and then match on that value using policy routing to have those packets delivered locally.

  -- TProxy Kernel Module Documentation

The following sections will describe the *IPTables* and policy routing rules  that are essential to make *Zorp* operable.

IPTables
========

At least the following *IPTables* ruleset is required for *Zorp*. Note that this ruleset is fair enough for *Zorp*, but it is inadequate for even the simplest firewall. The ruleset submits a working example of *Zorp*, so it must be extended with some other rules that are ordinary in case of a proxy firewall (for example: grant *SSH* access, handle *ICMP* messages). 

.. literalinclude:: configs/firewall.rules
  :language: none
  :emphasize-lines: 5-6,21,24,32,36

[*KZorp* related *IPTables* rules]

1. The ``socket`` matcher inspects the traffic by performing a socket lookup on the packet (non-transparent sockets are not counted) and checks if an open socket can be found. It practically means that *Zorp* (or any other application) has a socket for the traffic, it is already handled by *Zorp* in the userspace, no kernel-level intervention is required. In this case it is marked with the *TProxy mark* value (``0x80000000``), meaning that it should be handled by *Zorp*.
2. There are some chains of table ``mangle`` where *KZorp* must be hooked for certain purposes (rule evaluation, NAT handling, ...). In these cases we are jumping to a user-defined chain (``DIVERT``) where the corresponding rules can placed to pass the traffic to *KZorp* or even bypass it.
3. This is the place where we can put rules which match to certain traffic should be hidden from *KZorp* and accept it.
4. If no rule has been matched in this chain earlier, this rule jumps to *KZorp* and also marks the packet. This mark can be used in policy routing rules to divert traffic locally to *Zorp* instead of forwarding it to its original address. Note that this mark is the same that we use in case of the first rule of the ``PREROUTING`` chain.
5. If the traffic has already been marked in table ``mangle`` with the corresponding value (``0x80000000``), we should accept it. For example the data channel connection of active mode FTP matches the first rule of ``mangle`` table ``PREROUTING`` chain, so it has been marked, but should be accepted in the ``INPUT`` chain of ``filter`` table as it is an incoming connection.
6. The ``service`` matcher looks up services specified within *KZorp*. Services can be identified by name or by type. Type ``forward`` means a forwarded session (or *PFService*). These kind of sessions should be forwarded in the ``FORWARD`` chain of the ``filter`` table.

.. caution::
  The ruleset above contains those and only those rules which are essential to make *KZorp* and *Zorp* operable. The ruleset must be extended with other rules that make the firewall operable (for example: accepting incoming *SSH* connection or particular typed *ICMP* packets).

.. note::
  The ruleset above is IP version-independent, so it can be used both in case of ``iptables`` and ``ip6tables``.

Advanced Routing
================

Packets have been marked to a certain value in *IPTables*. Now match on that value using policy routing to have those packets delivered locally to *Zorp* instead of forwarding it to the original address, and *Zorp* will connect to a server depending on the policy.

.. literalinclude:: configs/rc.local
  :language: none

[*Zorp* related policy routing rules]

1. Rule instructs the system to lookup route for the traffic from table ``tproxy`` if the traffic has been marked with the required value (``0x80000000``) in the ``DIVERT`` chain of the ``mangle`` table in *IPTables*.
2. Table ``tproxy`` has only one route that diverts the traffic locally to *Zorp*, so it is not forwarded as it would have been done by default.

Table name ``tproxy`` can be used only if the following line is added to ``rt_tables`` file.

.. literalinclude:: configs/rt_tables
  :language: none

[*Zorp* related policy routing table names]

.. note::
  The policy routing rules above must be repeated with options ``-6`` instead of ``-4`` to make IPv6 operable.

Zorp
====

Kernel Module
-------------

As it is possible to use *kZorp* separately from *Zorp* using your *zones* in your IPTables rule set by *zone match* without *Zorp*. As the *zones* handled by the *kZorp* they must be downloaded to the kernel space. The init script of the ``iptables.utils`` does this by reading the *zone* descriptions from the file ``/etc/iptables.zones``. The syntax of the configuration file is the following.

.. code-block:: bash

  "intra";;10.0.0.0/8,fec0::/16
  "intra.devel";"intra";10.1.0.0/16,fec0:1::/24
  "intra.it";"intra";10.2.0.0/16,fec0:2::/24

If you do not use *zone match* in your IPTables rules this file can be omitted *Zorp* are going to download *zones* to *kZorp*.

.. versionadded:: 5.0
   The ``zones.py`` file.

Definition of *zones* moved to a separate file named ``/etc/zorp/zones.py`` and handled by a standalone daemon which downloads them to *kZorp*. If you don't use *zones* neither in your IPTables rule set nor in your *Zorp* policy the configuration file can be omitted. The syntax of the configuration file is the same as it has been mentioned Zone section (see also).

The configuration of the application level firewall itself has two completely different approaches.

#. configuration of the firewall application
#. description of the network security policy

Zorp Instance
-------------

As it has already mentioned parameters of the firewall application instances are stored in the configuration file named ``/etc/zorp/instances.conf``. It must exist, but can be empty, but practically the minimal configuration should contain at least one *Zorp* *instance* descriptions in order to make it possible being to run a *Zorp* process.

.. literalinclude:: configs/minimal_instances.conf
  :language: bash

If you do not have performance or debugging issues it is fair enough for smaller size configurations.

Network Security Policy
-----------------------

A *Zorp* policy contains same number of instance definition that has been declared in the configuration file ``instances.conf``. Practically it means at least one definitions as you can see in the following example.

.. literalinclude:: configs/minimal_policy.py
  :language: python
  :emphasize-lines: 3,5,7

[Minimal *Zorp* policy]

1. The ``Zorp.Core`` module contains the import of the mandatory classes (for example ``Rule``, ``Service``) so it must be imported.
2. Every *instance* represented as a Python function in the ``policy.py`` where the name of the function is the name of the corresponding *instance*. The function must not have any arguments.
3. In Python the ``pass`` does nothing. It can be used when a statement is required syntactically but the program requires no action. In this minimal case there is no definition (for example ``Service``) relates to our *instance*, so ``pass`` is used to indicate that fact.

This configuration result a running *Zorp* instance which does absolutely nothing considering the fact that there is no *rule* in the instance, so there is no *service* which can be launched. The trivial question arises as whether the ongoing traffic will be accepted or dropped. It depends on your IPTables rule set as the *kZorp* does not know what to do with the traffic so it does nothing with the traffic, neither accept nor drop it.

.. caution::

  There is two possible result of jumping to the ``KZORP`` target from IPTables.

  a. there is *rule* which matches to the traffic, so the packet will be

   * accepted if the *service* class is a ``PFService`` or ``Service``

   * rejected if  *service* class is ``DenyService``

  b. there is no *rule* matching to the traffic, so traffic will be accepted

  where

  * accept means that the packet will be put back right after the IPTables rule jumped to ``KZORP`` target and will be handled by one of the IPTables rules in the chain or the default policy
  * reject means that that the IPTables rule jumped to ``KZORP`` cause ``DROP`` or ``REJECT`` depending on the settings of the ``DenyService``

However there is no policy in the semantics of *Zorp* as it is in IPTables, a *rule* without any conditions always matches worst (see also) and it will be evaluated only when there is no other *rule* that matches better, so you can regard it as default.

To implement something like the ``DROP`` policy means in an IPTables chain, you should add a *rule* without any condition and ``DenyService`` as a *service*. You can also implement the ``REJECT`` IPTables policy if you change the necessary settings in the ``DenyService`` from ``DROP`` to ``REJECT``.

.. literalinclude:: configs/drop_all_policy.py
  :language: python

[Default drop *rule* in a *Zorp* policy]

Default accept can be easily implement by changing the ``DenyService`` to a ``PFService`` as it forwards the traffic just like the IPTables would do it.

.. note::

  Theres is need to add this kind of default rule if your IPTables policy is ``DROP`` or ``REJECT`` as it is suggested.

.. caution::

  If you use this method there is not possible do anithing with the packet (for example log) in the IPTables as it is dropped or rejected.

.. literalinclude:: configs/accept_all_policy.py
  :language: python

[Default accept *rule* in a *Zorp* policy]

.. caution::

  It is not recommended to use this method for the same reason as it is not recommended in case of IPTables.
