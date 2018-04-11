# Requirements
- Python 3.6.5
- TensorFlow 1.7

# Setup
## Install

```sh
sudo easy_install pip

sudo pip install --upgrade virtualenv

virtualenv --system-site-packages -p python3 .

pip3 install --upgrade tensorflow
```

## Start

```sh
source ./bin/activate
```

## Stop

```sh
source deactivate
```

# Check

```sh
python3 -V
python3 -c 'import tensorflow as tf; print(tf.__version__)'
```
