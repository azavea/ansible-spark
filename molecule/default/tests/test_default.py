import os
import re
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.common
def test_spark_user_dir_exists(host):
    f = host.file('/var/lib/spark/')
    assert f.exists


@pytest.mark.common
def test_spark_defaults_conf(host):
    f = host.file('/usr/lib/spark/conf/spark-defaults.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.mode == 0o644
    assert f.contains('spark.master')


@pytest.mark.common
def test_spark_env_sh(host):
    f = host.file('/usr/lib/spark/conf/spark-env.sh')

    assert f.exists
    assert f.user == 'root'
    assert f.mode == 0o644
    assert f.contains('LD_LIBRARY_PATH=')
    assert f.contains('SPARK_LOG_DIR=')
    assert f.contains('SPARK_PID_DIR=')
    # following env var is set only if 'spark_local_dirs' is configured
    assert f.contains('SPARK_LOCAL_DIRS=')
    assert f.contains('SPARK_LOCAL_DIRS="${SPARK_LOCAL_DIRS:-/tmp}"')


@pytest.mark.common
def test_spark_log4j_properties(host):
    f = host.file('/usr/lib/spark/conf/log4j.properties')

    assert f.exists
    assert f.mode == 0o644
    assert f.contains('log4j.rootCategory=')
    assert f.contains('log4j.appender.console=')
    assert f.contains('log4j.logger.org.apache.spark.repl.Main')


@pytest.mark.common
def test_spark_running_SparkPi(host):
    sparkTasks = 100
    sparkParams = ''
    sparkCmd = 'cd /usr/lib/spark/bin ; ./run-example {} SparkPi {}'.format(sparkParams, sparkTasks)
    out = host.check_output(sparkCmd)

    assert re.match("^Pi is roughly 3.14[0-9]+", out)
    # a successful job will return a rough estimation of Pi like
    #Pi is roughly 3.1412735141273
