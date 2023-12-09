def test_config():
    config = {
        'username': 'john',
        'password': 'secret'
    }
    
    assert config['username'] == 'john'
    assert config['password'] == 'secret'
