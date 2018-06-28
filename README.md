# ansible-spark

An Ansible role for installing [Apache Spark](https://spark.apache.org).

## Role Variables

- `spark_version` - Spark version.
- `spark_install_java` - Flag toggling the JDK installation using the builtin azavea.java role dependency (default: `True`)
- `spark_cloudera_distribution` - Cloudera distribution version (default: `cdh5.4`)
- `spark_symlinks_enabled` - If `True` deploy 2 symlinks (<spark_home>/conf -> /etc/spark/conf ; <spark_home> -> `spark_usr_dir` ) (default `True`) 
- `spark_shims_enabled` - If `True` deploy the shims (like `/usr/bin/spark-shell`, `/usr/bin/spark-submit`) (default `True`)
- `spark_env_extras` - An optional dictionary with key and value attributes to add to `spark-env.sh` (e.g. `MESOS_NATIVE_LIBRARY: "/usr/local/lib/libmesos.so"`)
- `spark_defaults_extras` - An optional dictionary with key and value attributes
  to add to `spark-defaults.conf` (e.g. `"spark.eventLog.enabled": True`)
- `spark_user_groups` - An optional list of (OS)groups the spark user should belong to
- `spark_user_shell` - The spark user's default shell (default: `/bin/false`)
- `spark_log4j_loggers` - A list of dictionaries configuring the spark log4j loggers (default: logger config from spark/conf/log4j.properties.template)
- `spark_hdfs_native_lib_path` - Path for the HDFS library folder (default: `/usr/lib/hadoop/lib/native`)

## Example Playbook

See the [examples](./examples/) directory.
