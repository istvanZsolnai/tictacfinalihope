def winsound():
    import os
    duration = 0.2  # second
    freq = 400  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.2  # second
    freq = 500  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.2  # second
    freq = 600  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

def loosersound():
    import os
    duration = 0.3  # second
    freq = 400  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.3  # second
    freq = 300  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.3  # second
    freq = 200  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))

def tiesound():
    import os
    duration = 0.2  # second
    freq = 600  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.2  # second
    freq = 500  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.2  # second
    freq = 400  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
    duration = 0.2  # second
    freq = 600  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
