----
Zorp
----

*Zorp GPL* is a next generation, open source proxy firewall with deep protocol analysis. It allows you to inspect, control, and modify traffic on the application layer of the ISO/OSI model. Decisions can be made based on data extracted from the application-level traffic (for example, HTTP) and applied to a certain traffic type such as users or client machines. It ensures that the traffic complies with the particular protocol standards, and allows you to perform specific actions with the traffic.

Why choose it?

* Free license and active community support
* Network traffic analysis in 7 protocols
* Encrypted channel control
* Content filtering and optional modification
* Modular, highly flexible configuration
* The only answer to many unique problems
* Established project with a 10-year history

Features
========

Access control
  Access control in *Zorp GPL* has a lot more possibilities than average firewalls. It is based on zones instead of hosts or IP ranges and besides “who” and “what”, it can also limit “how”. For example, clients arriving from one zone can only read a given FTP server, whereas others have write privileges.

Information leakage prevention
  Information leakage prevention helps to keep sensitive information inside your network. For example, HTTP data flow could include internal IP addresses, the URL of a previously visited website (referrer), or browser and operating system information (agent). *Zorp GPL* is able remove or change this information.

Content filtering
  Content filtering is done by using external applications, like virus scanners, spam filters and URL checkers. Connections can be accepted, rejected or just simply logged. Suspicious content can be quarantined. *Zorp GPL* can integrate with all popular antivirus engines, such as NOD32 or AMaVIS.

  Supported protocols:

  * wildly used procols: *HTTP*, *FTP*, *SMTP*, *POP3*
  * rarely used: *Finger*, *Whois*, *Telnet*
  * secure: *HTTPS*, *FTPS*, *POP3S*, *SMTPS*

Audit
  Audit of all events is possible, even requests and responses of a protocol, as proxies work at the application level. This can prove not only what happened, but also what did not, for example an old version of a file was deleted, but never uploaded again.

Interoperability
  Interoperability helps in a world where not all protocol implementation is created equal. *Zorp GPL* is able to hide protocol features, like compression from HTTP, translate between different encryption standards, and other changes to make clients and servers interoperate more easily.

Flexibility
  Flexibility is a key feature of *Zorp GPL*. It is easily extendable by additional modules and customizable to solve specific security problems.

Linux support
  *Zorp GPL* administrators can compile and run the product on several Linux-based operating systems. Besides that, pre-compiled binaries are readily available on various Linux distributions, which greatly simplifies its installation on these platforms. Currently binary repositories are available for the following distributions:

  * *Debian*: squeeze, unstable; (i386, amd64)
  * *Ubuntu*: from 10.04 (i386, amd64)

Community
=========

Please join our increasing *Zorp GPL* community by subscribing to one or more of the following forums.

* `FaceBook <https://www.facebook.com/pages/Zorp-GPL/239692256091025>`_
* `Google+ <https://plus.google.com/115296005910438881857>`_
* `LinkedIn <http://www.linkedin.com/groups/Zorp-GPL-4166962>`_
* `Twitter <https://twitter.com/ZorpGPL>`_

Downloads
=========

Sources
^^^^^^^

* `Zorp GPL <http://github.com/balabit/zorp>`_, the firewall itself
* `kZorp <http://github.com/balabit/kzorp>`_, kernel module
* `libzorpll <http://github.com/balabit/libzorpll>`_, low-level networking library

Binaries
^^^^^^^^

* *Zorp GPL* packages from `Debian <http://packages.debian.org>`_ and `Ubuntu <http://packages.ubuntu.com>`_ distribution
* *Zorp GPL* and related packages for Debian and Ubuntu distribution on `MadHouse Project <http://asylum.madhouse-project.org/projects/debian>`_

Support
=======

Mailing lists
^^^^^^^^^^^^^

* Subscribe to the lists directly in `English <https://lists.balabit.hu/mailman/listinfo/zorp>`_ or `Hungarian <https://lists.balabit.hu/mailman/listinfo/zorp>`_
* List archives are available at the above URLs

Documentation
^^^^^^^^^^^^^

* `Zorp GPL Tutorial <http://zorp-gpl-tutorial.readthedocs.org>`_ on ReadTheDocs
* `Configuration examplesGitHub <http://github.com/balabit/zorp-examples>`_ on GitHub

Evaluate
^^^^^^^^

There is a set of `virtual machines <http://people.balabit.hu/szilard/zorp-gpl/virtual-machines/>`_ to test *Zorp GPL*.

License
=======

* *Zorp GPL* is licensed under `GPL 2.0 <http://www.gnu.org/licenses/gpl-2.0.html>`_
* *kZorp* is licensed under `GPL 2.0 <http://www.gnu.org/licenses/gpl-2.0.html>`_
* *libzorpll* is licensed under `LGPL 2.0 <http://www.gnu.org/licenses/lgpl-2.0.html>`_
