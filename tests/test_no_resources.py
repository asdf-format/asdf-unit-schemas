import asdf


def test_no_resources():
    resource_manager = asdf.get_config().resource_manager
    for uri, mapping in resource_manager._mappings_by_uri.items():
        assert mapping.package_name != "asdf-unit-schemas"
