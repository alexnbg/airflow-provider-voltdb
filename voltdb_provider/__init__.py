def get_provider_info():
    return {
        "package-name": "airflow-provider-voltdb",
        "name": "VoltDB Airflow Provider",
        "description": "VoltDB provider package for Apache Airflow.",
        "hook-class-names": [
            "voltdb_provider.hooks.base_voltdb_hook.BaseVoltDBHook"
        ],
        "connection-types": [
            {
                "connection-type": "voltdb",
                "hook-class-name": "voltdb_provider.hooks.base_voltdb_hook.BaseVoltDBHook"
            }
        ],
        # "extra-links": ["voltdb_provider.operators.sample_operator.ExtraLink"],
        "versions": ["1.0.2"]
    }
