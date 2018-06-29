# ansible-spark

An Ansible role for installing [Apache Spark](https://spark.apache.org).

## Role Variables

- `spark_version` - Spark version.
- `spark_install_java` - flag toggling the JDK installation using the builtin azavea.java role dependency (default: `yes`)
- `spark_symlinks_enabled` (default `yes`) - if `yes` deploy 2 symlinks (<spark_home>/conf -> /etc/spark/conf ; <spark_home> -> `spark_usr_dir` )
- `spark_shims_enabled` (default `yes`) - if `yes` deploy the shims (like `/usr/bin/spark-shell`, `/usr/bin/spark-submit`)
- `spark_env_extras` - An optional dictionary with key and value attributes to add to `spark-env.sh` (e.g. `MESOS_NATIVE_LIBRARY: "/usr/local/lib/libmesos.so"`)
- `spark_defaults_extras` - An optional dictionary with key and value attributes
  to add to `spark-defaults.conf` (e.g. `"spark.eventLog.enabled": true`)
- `spark_user_group` - The Spark user's primary group
- `spark_user_groups` - an optional list of (OS)groups the spark user should belong to
- `spark_user_shell` - the spark user's default shell (default: `/bin/false`)
- `spark_log4j_loggers` - A list of dictionaries configuring the spark log4j loggers (default: logger config from spark/conf/log4j.properties.template)
- `spark_hdfs_native_lib_path` - Path for the HDFS library folder (default: `/usr/lib/hadoop/lib/native`)

## Example Playbook

See the [examples](./examples/) directory.
