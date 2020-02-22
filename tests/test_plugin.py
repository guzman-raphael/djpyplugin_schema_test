from datajoint.plugin import schema_plugins


def test_check_plugin_status():
    assert(schema_plugins['raphael_adapted_graph']['verified'])
