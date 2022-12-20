from distutils.core import setup, Extension

accimage = Extension(
    "accimage",
    # include_dirs=["/usr/local/opt/jpeg-turbo/include", "/opt/intel/ipp/include"],
    include_dirs=["C:/libjpeg-turbo64/include", "C:/acclib/ipp/include"],
    libraries=["jpeg", "ippi", "ipps"],
    library_dirs=["C:/libjpeg-turbo64/lib", "C:/acclib/ipp/Library/lib"],
    sources=["accimagemodule.c", "jpegloader.c", "imageops.c"],
)

setup(
    name="accimage",
    version="0.2.0",
    description="Accelerated image loader and preprocessor for Torch",
    author="Marat Dukhan",
    author_email="maratek@gmail.com",
    ext_modules=[accimage],
)
