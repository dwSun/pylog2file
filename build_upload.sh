rm -rvf build
rm -rvf dist
python setup.py check
python setup.py sdist
twine check dist/log2file-*.tar.gz
twine upload dist/log2file-*.tar.gz
