##########################
Performance Considerations
##########################

The Fragalysis Stack consists of two main components - a *Stack* and a *Worker*.
Both are deployed to Kubernetes as separate **Pods** each controlled by their
own **StatefulSet**. The *Stack* Pod essentially acts as the Django application's
front-end and REST API responder. This Pod responds to requests in a synchronous manner.
Any request it receives that can may result in significant processing (like the upload
or download of a Target) is delegated to a *Task* (managed by `Celery`_) that is
executed separately, in a *Worker* Pod.

The *Stack* and *Worker* Pods cannot handle unlimited workloads - they are limited
using **Replicas**, **Concurrency**, **Memory** and **CPU** *budgets*, described below.

Because processing capacity is restricted in these ways you must decide
whether the defaults are suitable for your installation.

The default settings will create two *Stack* and *Worker* Pods, each able to
satisfy up to ``4`` concurrent asynchronous *Worker* Tasks and *Stack* API requests,
providing support for ``8`` concurrent Tasks or API requests that can consume
approximately ``16`` gigabytes of RAM.

The various playbook control variables are described in the following sections.

********
Replicas
********

Replica values limit the number of each Pod type.

- Stack: ``stack_replicas`` (default ``2``)
- Worker: ``worker_replicas`` (default ``2``)

***********
Concurrency
***********

Concurrency values limit the number of concurrent processes within each Pod type.
When these limits are exceeded further requests and Tasks will be blocked.

- Stack: ``stack_concurrency`` (default ``4``)
- Worker: ``worker_concurrency`` (default ``4``)

*********************
Memory and CPU Budget
*********************

When adjusting a Pod's concurrency you will need to pay attention to the Memory
and CPU resource allocated to the corresponding Pod type. If you support more Tasks
you might need more memory and more CPU to permit the increased concurrency.

There are separate control variables for the *Stack* and *Worker* Pods, and each CPU and
Memory definition is defined in two variables - a *request* and a *limit*. The request
is what you consider as being a reasonable *steady state* value - i.e. the value
required to operate comfortably under normal load.
The *limit* is a hard-limit that Kubernetes will enforce.

.. note::
    Your Pod will not be able to exceed the CPU *limit* and if your Pod exceeds the
    Memory *limit* it will be terminated by Kubernetes.

The corresponding Ansible control variables for the *Stack* are: -

- CPU request: ``stack_cpu_request`` (default ``250m``, 1/4 Core)
- CPU limit: ``stack_cpu_limit`` (default ``4``)
- Memory request: ``stack_memory_request`` (default ``16Gi``)
- Memory limit: ``stack_memory_request`` (default ``16Gi``)

The corresponding Ansible control variables for the *Worker* are: -

- CPU request: ``worker_cpu_request`` (default ``250m``, 1/4 Core)
- CPU limit: ``worker_cpu_limit`` (default ``4``)
- Memory request: ``worker_memory_request`` (default ``16Gi``)
- Memory limit: ``worker_memory_request`` (default ``16Gi``)

.. note::
    These Memory and CPU values are empirical. You should perform your own performance
    investigations in order to determine practical values for your installation
    and workload.

.. _celery: https://pypi.org/project/celery/
