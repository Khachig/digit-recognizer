from abc import ABC, abstractmethod
from binascii import b2a_hex as bth

def to_int(bytestring):
    return int(bth(bytestring), 16)

class Parser(ABC):
    def __init__(self, data_file):
        self.data_file = data_file

    @abstractmethod
    def parse(self):
        raise NotImplementedError


class ImageParser(Parser):
    def parse(self):
        with open(self.data_file, 'rb') as dtf:
            # The file format is described on the MNIST webpage: yann.lecun.com/exdb/mnist/
            # In this case, the magic number isn't necessary so we can discard the first 4 bytes
            dtf.seek(4)
            num_images = to_int(dtf.read(4))
            num_rows = to_int(dtf.read(4))
            num_cols = to_int(dtf.read(4))
            num_pixels = num_rows * num_cols

            # iterate <num_images> times and read <num_rows> * <num_cols> values as one image
            # convert the pixel data to int before writing to list
            for _ in range(num_images):
                image = [to_int(dtf.read(1)) for _ in range(num_pixels)]
                yield image


class LabelParser(Parser):
    def parse(self):
        with open(self.data_file, 'rb') as dtf:
            # The file format is described on the MNIST webpage: yann.lecun.com/exdb/mnist/
            # In this case, the magic number isn't necessary so we can discard the first 4 bytes
            dtf.seek(4)
            num_labels = to_int(dtf.read(4))

            for _ in range(num_labels):
                yield to_int(dtf.read(1))

