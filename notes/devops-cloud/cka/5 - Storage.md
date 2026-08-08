# 5 - Storage

## Quick Summary

Kubernetes storage separates a Pod's need for storage from the actual storage implementation. CKA expects you to understand volume types, PersistentVolumes, PersistentVolumeClaims, StorageClasses, access modes, reclaim policies, and dynamic provisioning.

## Beginner Bridge

Containers are replaceable, so files written inside the container filesystem should not be treated as durable data.

Kubernetes storage has two broad cases:

```text
Temporary files for a Pod lifetime -> ephemeral volume, such as emptyDir
Durable files beyond Pod lifetime -> PersistentVolumeClaim backed by PersistentVolume
```

For persistent storage, the application usually asks for a PVC. The cluster then binds that request to real storage, often created dynamically through a StorageClass. When storage fails, inspect both the Pod and the PVC because the app and the storage request can fail independently.

## Why Storage Matters

Containers are replaceable. Pods can be recreated on different nodes. Without persistent storage, data written inside a container filesystem can disappear when the container or Pod is replaced.

Use Kubernetes storage when:

- A database needs durable data.
- An app needs shared files.
- A backup/restore tool writes persistent output.
- A workload needs config/certificates as mounted files.

## Core Concepts

| Concept | Meaning |
| --- | --- |
| Volume | Storage attached to a Pod. |
| PersistentVolume (PV) | Cluster-level storage resource. |
| PersistentVolumeClaim (PVC) | User request for storage. |
| StorageClass | Defines dynamic provisioning behavior. |
| Access mode | How a volume can be mounted, such as read-write by one node. |
| Reclaim policy | What happens to PV after PVC is deleted. |

## Ephemeral Volumes

Ephemeral storage is tied to Pod lifetime.

Common examples:

| Type | Use |
| --- | --- |
| `emptyDir` | Scratch space shared by containers in a Pod. |
| `configMap` | Mount ConfigMap data as files. |
| `secret` | Mount Secret data as files. |
| `downwardAPI` | Expose Pod metadata to files/env. |

`emptyDir` example:

```yaml
volumes:
  - name: cache
    emptyDir: {}
containers:
  - name: app
    image: nginx
    volumeMounts:
      - name: cache
        mountPath: /cache
```

If the Pod is deleted, the `emptyDir` data is deleted.

## PersistentVolumes And Claims

PVC requests storage:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: app-data
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: standard
```

Pod uses the claim:

```yaml
volumes:
  - name: data
    persistentVolumeClaim:
      claimName: app-data
containers:
  - name: app
    image: nginx
    volumeMounts:
      - name: data
        mountPath: /usr/share/nginx/html
```

## StorageClasses

StorageClass defines how storage is dynamically provisioned.

Inspect:

```bash
kubectl get storageclass
kubectl describe storageclass <name>
```

Example:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: example.com/fast-storage
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

Important fields:

| Field | Purpose |
| --- | --- |
| `provisioner` | Storage plugin/driver. |
| `reclaimPolicy` | Delete or retain PV after claim deletion. |
| `volumeBindingMode` | When binding/provisioning happens. |
| `allowVolumeExpansion` | Whether PVC expansion is allowed. |

## Dynamic Provisioning

Dynamic provisioning means Kubernetes automatically creates a backing volume when a PVC requests a StorageClass.

Flow:

```text
PVC created -> StorageClass selected -> CSI/provisioner creates volume -> PV appears -> PVC bound -> Pod mounts volume
```

If PVC stays `Pending`, check:

```bash
kubectl describe pvc <name>
kubectl get storageclass
kubectl get events --sort-by=.lastTimestamp
```

## Static Provisioning

Static provisioning means an admin creates PVs manually.

Example:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: manual-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual
  hostPath:
    path: /data/manual-pv
```

`hostPath` is useful for labs, but it is not a good general production storage pattern because it ties data to one node.

## Access Modes

| Mode | Meaning |
| --- | --- |
| ReadWriteOnce | Volume can be mounted read-write by a single node. |
| ReadOnlyMany | Volume can be mounted read-only by many nodes. |
| ReadWriteMany | Volume can be mounted read-write by many nodes. |
| ReadWriteOncePod | Volume can be mounted read-write by a single Pod. |

Access mode support depends on the storage driver.

## Reclaim Policies

| Policy | Meaning |
| --- | --- |
| Retain | PV remains after PVC deletion. Admin must handle cleanup/reuse. |
| Delete | Backing storage is deleted when claim is deleted. |

Be careful with `Delete` for important data.

## Volume Binding Mode

| Mode | Meaning |
| --- | --- |
| Immediate | Volume is bound/provisioned as soon as PVC is created. |
| WaitForFirstConsumer | Binding waits until a Pod needs the PVC, allowing topology-aware placement. |

`WaitForFirstConsumer` is important for zonal storage because the selected volume zone must match the node zone.

## CSI

Container Storage Interface lets storage vendors integrate with Kubernetes.

CSI commonly supports:

- Dynamic provisioning.
- Volume attach/detach.
- Mount/unmount.
- Snapshots if supported.
- Expansion if supported.

## Benefits

- Separates storage request from implementation.
- Supports dynamic provisioning.
- Lets Pods move while preserving data where storage supports it.
- Standard interface through CSI.
- Works with many cloud and on-prem storage systems.

## Drawbacks / Limitations

- Storage behavior depends heavily on the driver.
- Access modes are not always supported by every backend.
- Stateful workloads require backup, restore, and disaster recovery planning.
- `hostPath` is unsafe for general production use.
- Storage can constrain scheduling by zone or node.

## Hidden Details / Caveats

- PVC namespace matters; Pods can only use PVCs in the same namespace.
- PVs are cluster-scoped; PVCs are namespaced.
- A PVC may stay `Pending` because of StorageClass, quota, topology, or missing provisioner.
- Deleting a PVC can delete real backing storage if reclaim policy is `Delete`.
- Mounting a ConfigMap or Secret as a volume differs from using it as environment variables.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Expecting container filesystem to persist | Use a PVC. |
| Using `hostPath` for production data | Use CSI-backed persistent storage. |
| Wrong StorageClass name | Check `kubectl get storageclass`. |
| Access mode unsupported | Verify driver capabilities. |
| PVC in wrong namespace | Create/use PVC in the same namespace as the Pod. |
| Deleting PVC without checking reclaim policy | Inspect PV/StorageClass first. |

## Troubleshooting

```bash
kubectl get pv
kubectl get pvc -A
kubectl describe pvc <name>
kubectl describe pv <name>
kubectl get storageclass
kubectl get events --sort-by=.lastTimestamp
```

| Symptom | Likely Cause |
| --- | --- |
| PVC `Pending` | Missing StorageClass, no provisioner, quota, topology issue. |
| Pod stuck `ContainerCreating` | Volume attach/mount problem. |
| Permission denied | Filesystem ownership, security context, storage backend permissions. |
| Data disappeared | Used ephemeral storage or deleted PVC with `Delete` reclaim policy. |

## Interview Notes

- PV is cluster-scoped; PVC is namespaced.
- StorageClass enables dynamic provisioning.
- Reclaim policy controls what happens after claim deletion.
- Access modes describe mount semantics but depend on storage backend support.
- `WaitForFirstConsumer` helps with topology-aware provisioning.
- CSI is the standard storage plugin interface.

## Related Topics

- [3 - Workloads and Scheduling](3%20-%20Workloads%20and%20Scheduling.md)
- [6 - Troubleshooting](6%20-%20Troubleshooting.md)

## Official References

- [Kubernetes storage](https://kubernetes.io/docs/concepts/storage/)
- [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
