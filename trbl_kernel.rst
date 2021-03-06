Kernel debugging
================

Dynamic debugging
-----------------

If the dynamic debugging is enabled in your kernel configuration, *KZorp* debug messages can be enabled and disabled dynamically. Before enabling any debug messages or leaving them enabled, consider the fact that logging these messages may cause serious performance issues especially in case of heavy traffic. 

.. code:: bash

  echo 'file kzorp_netlink.c +p' > /sys/kernel/debug/dynamic_debug/control # <1>
  echo 'module kzorp +p'         > /sys/kernel/debug/dynamic_debug/control # <2>

1. Enables debug messages in source file ``kzorp_netlink.c``
2. Enables debug messages ``kzorp`` module

Debug messages can be disabled with the same command, using the ``-p`` switch after the name of the source file or module instead of ``+p``. For details, read the `dynamic debug howto <https://www.kernel.org/doc/Documentation/dynamic-debug-howto.txt>`_.

Function tracer
---------------

If the dynamic debugging support is not enabled in our kernel, there is another possibility to trace *KZrop*, the kernel part of *Zorp*. Functions are traced whether there are debug messages in them or not. *KZorp* related functions have a ``kz_`` prefix in their names, so tracing them can be enabled with the following commands:

.. code:: bash

  sysctl kernel.ftrace_enabled=1 # <1>
  
  cd /sys/kernel/debug/tracing
  echo function_graph > current_tracer # <2>
  echo 'kz_*' > set_ftrace_filter # <3>
  
  echo 0 > tracing_on # <4>
  sleep 1
  echo 1 > tracing_on # <5>

1. Checks that ``ftrace_enabled`` is set in the kernel configuration, otherwise this tracer is a nop.
2. Sets the tracer that provides the ability to draw a graph of function calls similar to *C* code.
3. Limits tracing to functions with names starting with the ``kz_`` prefix.
4. Starts the tracing.
5. Stops the tracing.

The result of the trace can be read in the ``trace`` file. For details, read the `function traces documentation <https://www.kernel.org/doc/Documentation/trace/ftrace.txt>`_.
