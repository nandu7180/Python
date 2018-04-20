def ask_ok(promt, retries=4, cpmplint='yes or no, please!'):
    while True:
        ok = raw_input(promt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False

        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print cpmplint


ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
