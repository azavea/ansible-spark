## 1.2.0

- Add backward compatible support with Ansible 2.0.
- Ensure that example uses YAML role specification format.

## 1.1.0

- Add configurable Spark user and group.
- Add support for a custom installation directory.
- Add support for settng `spark-defaults.conf`.

## 1.0.0

- Use Apache as the source for Spark vs. Cloudera. This change breaks backward
  compatibility with roles < 1.0.0.

## 0.3.0

- Bump Spark version to `1.3.0`.
- Add `spark_cloudera_distribution` variable to determine which package
  distribution channel is used.

## 0.2.0

- Add ability to set arbitrary environment variables in `spark-env.sh`

## 0.1.2

- Fix Hadoop configuration file reference in `spark-env.sh`.

## 0.1.1

- Bump Spark version to `1.2.0+cdh5.3.0+364-1.cdh5.3.0.p0.36~trusty-cdh5.3.0`.

## 0.1.0

- Initial release.
