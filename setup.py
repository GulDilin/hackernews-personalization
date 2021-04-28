import subprocess
import sys
import os


def install(file):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file])


def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])


if __name__ == '__main__':
    install(os.path.join(os.path.abspath(os.path.curdir), 'requirements.txt'))
    import nltk

    nltk.download('punkt')
    nltk.download('wordnet')
    nltk.download('stopwords')
