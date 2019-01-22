import os
import zipfile
import re


def zip(src, dst):
    zf = zipfile.ZipFile('%s.zip' % dst, 'w', zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            zf.write(absname, arcname)
    zf.close()


def unzip(src, dst):
    zf = zipfile.ZipFile(src, 'r')
    zf.extractall(dst)
    zf.close()


def find_file(src):
    for root, dirs, files in os.walk(src):
        for file_name in files:
            if file_name == "presentation.xml":
                file_path = os.path.join(root, file_name)
                return file_path


def modify(src):
    with open(src, 'r') as file:
        filedata = file.read()

    line = re.sub(r"<p:modifyVerifier cryptProviderType.*/>", "", filedata)

    with open(src, 'w') as file:
        file.write(line)


if __name__ == '__main__':
    os.rename("files/claves-contexto.pptx", "files/a.zip")

    unzip("files/a.zip", "files/tmp/a/")
    file_path = find_file("files/tmp/a/")
    modify(file_path)
    zip("files/tmp/a/", "files/b")

    os.rename("files/b.zip", "files/b.pptx")