def get_provider_info():
    return {
        "package-name": "airflow-provider-voltdb",
        "name": "Airflow VoltDB Provider",
        "description": "Airflow provider for connection to VoltDB",
        "versions": ["1.0.3"],
        'integrations': [
            {
                'integration-name': 'VoltDB',
                'external-doc-url': 'https://docs.voltdb.com/',
                'tags': ['software'],
            }
        ],
        'hooks': [
            {
                'integration-name': 'VoltDB',
                'python-modules': ['voltdb_provider.hooks.base_voltdb_hook'],
            }
        ],
        "hook-class-names": ["voltdb_provider.hooks.base_voltdb_hook.BaseVoltDBHook"],
        "connection-types": [
            {
                "hook-class-name": "voltdb_provider.hooks.base_voltdb_hook.BaseVoltDBHook",
                "connection-type": "voltdb",
            }
        ],
    }
