# ansible-spark

An Ansible role for installing [Apache Spark](https://spark.apache.org).

## Role Variables

- `spark_version` - Spark version.
- `spark_cloudera_distribution` - Cloudera distribution version (default: `cdh5.4`)
- `spark_env_extras` - An optional dictionary with key and value attributes to add to `spark-env.sh` (e.g. `MESOS_NATIVE_LIBRARY: "/usr/local/lib/libmesos.so"`)

## Example Playbook

See the [examples](./examples/) directory.
