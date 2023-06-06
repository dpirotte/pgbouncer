import psycopg
import pytest


def test_host_strategy_last_successful_good_first(bouncer):
    with bouncer.log_contains(r"127.0.0.1:\d+ new connection to server", 1):
        bouncer.test(dbname="hostlist_good_first")
        bouncer.test(dbname="hostlist_good_first")

def test_host_strategy_last_successful_bad_first(bouncer):
    with bouncer.log_contains(r"127.0.0.3:\d+ closing because: connect failed", 1):
        with bouncer.log_contains(r"127.0.0.1:\d+ new connection to server", 1):
            bouncer.test(dbname="hostlist_bad_first")
            bouncer.test(dbname="hostlist_bad_first")
            bouncer.test(dbname="hostlist_bad_first")
