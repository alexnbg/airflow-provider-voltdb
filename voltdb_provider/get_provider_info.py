def get_provider_info():
    return {
        "package-name": "airflow-provider-voltdb",
        "name": "Airflow VoltDB Provider",
        "description": "Airflow provider for connection to VoltDB",
        "versions": ["1.0.2"],
        "hook-class-names": ["voltdb_provider.hooks.base_voltdb_hook.BaseVoltDBHook"],
        "connection-types": [
            {
                "hook-class-name": "voltdb_provider.hooks.base_voltdb_hook.BaseVoltDBHook",
                "connection-type": "voltdb"
            }
        ]
    }
