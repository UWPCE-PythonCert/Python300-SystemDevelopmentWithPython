import os, random, shutil

class TemporaryDirectory(object):
    def __init__(self,directory):
        self.base_directory = directory

    def __enter__(self):
        # set things up
        self.directory = self.base_directory + str(random.random()) + "/"
        os.makedirs(self.directory)
        return self.directory

    def __exit__(self, type, value, traceback):
        # tear it down
        shutil.rmtree(self.directory)

with TemporaryDirectory("/tmp/foo") as dir:
    # write some temp data into dir
    with open(dir+"foo.txt", 'wb') as f:
        import time
        f.write("foo")
        time.sleep(2)
