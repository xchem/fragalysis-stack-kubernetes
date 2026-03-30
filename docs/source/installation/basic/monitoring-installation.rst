#############################
Installing Monitoring (Basic)
#############################

We rely on Prometheus and Grafana for monitoring, which is typically installed
using the `kube-prometheus-stack`_ Helm chart. Once you have a ``KUBECONFIG`` and
access to the cluster installation is relatively simple, requiring just a name
(the unimaginative **kube-prometheus-stack** in the following example).

Run the following from the project root ``/monitoring`` directory,
where you will find a suitable ``dev-values.yaml`` configuration file.

    kubectl create namespace monitoring
    helm install -f dev-values.yaml kube-prometheus-stack \
        oci://ghcr.io/prometheus-community/charts/kube-prometheus-stack

This will install the application in the ``monitoring`` **Namespace** with some
persistence, and provide the following ingresses: -

-   https://alartmanager.xchem-dev.diamond.ac.uk/
-   https://grafana.xchem-dev.diamond.ac.uk/

To get the Grafana ``admin`` password run the following: -

    kubectl get secret --namespace monitoring \
        -l app.kubernetes.io/component=admin-secret \
        -o jsonpath="{.items[0].data.admin-password}" | base64 --decode ; echo

If using lens you will need to set the following properties of its "Metrics"
Cluster Settings in order to see _live_ CPU and Memory stats: -

-   **METRICS SOURCE** : ``Prometheus``
-   **PROMETHEUS** : ``Helm``
-   **Filter empty containers** : ``Un-checked``
-   **PROMETHEUS SERVICE ADDRESS** : ``monitoring/kube-prometheus-stack-prometheus:9090``

A similar set of values, for the production cluster, provide the following ingresses: -

-   https://alartmanager.xchem.diamond.ac.uk/
-   https://grafana.xchem.diamond.ac.uk/

*******************
Removing Monitoring
*******************

To remove monitoring, refer to the official `uninstall`_ guide.

You might also need to remove the Alert Manager PVC. Check the namespace and delete if
necessary: -

    kubectl delete pvc alertmanager-kube-prometheus-stack-alertmanager-db-alertmanager-kube-prometheus-stack-alertmanager-0 -n monitoring

And then delete the _custom_ namespace: -

    kubectl delete namespace monitoring

.. _kube-prometheus-stack: https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack
.. _uninstall: https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack#uninstall-helm-chart
