def test_get_config():
    config = get_config()
    assert config['name'] == 'simple_demo'
    assert config['version'] == '0.0.1'
    assert config['author'] == 'Your Name'
    assert config['author_email'] == ''