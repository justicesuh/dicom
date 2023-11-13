import pathlib

import cv2
import PIL
import pydicom as dicom


def get_dcm_images(path):
    for child in (pathlib.Path(path) / 'dcm').iterdir():
        if child.suffix == '.dcm':
            yield child.resolve()


def dcm2png(image):
    ds = dicom.dcmread(image)
    image = (image.parents[1] / 'png' / image.name).with_suffix('.png')
    image.parents[0].mkdir(exist_ok=True)
    cv2.imwrite(str(image), ds.pixel_array)


if __name__ == '__main__':
    for image in get_dcm_images('data'):
        dcm2png(image)
