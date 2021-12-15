secret_key = 'Th1s@one!seCret!'
secret_payload = {
                "name": 'test',
                "is_admin": 0,
                "secret_key": 'VGgxc0BvbmUhc2VDcmV0IQ=='
            }


def filter(flag):
    return flag.replace("[", '').replace("]", '')

