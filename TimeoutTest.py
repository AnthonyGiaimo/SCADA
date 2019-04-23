import msvcrt
import time
import sys


class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout, timer=time.monotonic):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
            if result[-1] == '\n':   #XXX check what Windows returns here
                return ''.join(result[:-1])
        time.sleep(0.04) # just to yield to other processes/threads
    raise TimeoutExpired

answer = ""

while answer != "exit":
    try:
        answer = input_with_timeout("type: ", 300)
    except TimeoutExpired:
        print('Sorry, times up')
    else:
        print('Got %r' % answer)