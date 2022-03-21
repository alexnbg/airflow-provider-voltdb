# This is needed to allow Airflow to pick up specific metadata fields it needs for certain features. We recognize it's a bit unclean to define these in multiple places, but at this point it's the only workaround if you'd like your custom conn type to show up in the Airflow UI.
def get_provider_info():
    return {
        "package-name": "airflow-provider-voltdb",  # Required
        "name": "VoltDB Airflow Provider",  # Required
        "description": "An airflow provider for connecting to VoltDB.",  # Required
        "hook-class-names": ["voltdb_provider.hooks.sample_hook.SampleHook"],
        "extra-links": ["voltdb_provider.operators.sample_operator.ExtraLink"],
        "versions": ["0.0.1"]  # Required
    }
