# Conda/pip environments

## How to setup a conda/pip base environment?

:::{note}
The following instructions are for Miniforge but should also work for the offline packages provided by the DeepModeling projects.
:::

An environment is a directory that contains a specific collection of packages that you have installed.
Different environments are isolated from each other.
A base environment is required before setuping up multiple environments.

First of all, download and execute [conda-forge installer](https://conda-forge.org/download/):

```sh
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh -O miniforge.sh
bash miniforge.sh -b -p $HOME/miniforge3
```

This will install the conda base environment into `$HOME/miniforge3`. You can install the environment into a different path.

After installation, you can activate the base environment using

```sh
source $HOME/miniforge3/bin/activate
```

In order to initialize the environment whenever starting the bash shell, run

```sh
conda init --all
```

Now you can use `conda install` or `pip install` command to install conda or pip packages.

## What is the difference between conda and pip?

The largest difference is that pip can only install Python packages,
but [conda](https://docs.conda.io/projects/conda/) can install any packages including C, C++, and Fortran packages without Python involved.
We suggest reading the [Anaconda blog](https://www.anaconda.com/blog/understanding-conda-and-pip) for more information.

## How can I check what packages have been installed?

Run `conda list` and `pip list`, which show all conda/pip packages that have been installed in the current environment.

## How to create a new conda/pip environment?

To create a conda/pip environment named `my_env`, run

```sh
conda create -n my_env python=3.11
```

Now you can activate the environment using

```sh
conda activate my_env
```

If you want to activate the environment in a shell script, using `shell` instead:

```sh
source activate my_env
```

## Why do I need multiple environments instead of one?

Due to multiple reasons, dependencies of packages often conflict with each other.
For example, Python 3.11 and 3.12 cannot be installed into the same environment;
CUDA 11 and CUDA 12 packages cannot be installed into the same environment;
Open MPI and MPICH cannot be installed into the same environment;
packages built against zlib 1.2 and 1.3 cannot be installed into the same environment.
While [conda-forge](https://conda-forge.org) has tried its best to reduce package conflicts, it may still happen when installing multiple packages.
Installing different packages into different environments will reduce the risk to meet the conflict packages.

## How to use conda to install CUDA packages without CUDA installed?

Usually, `conda` detects the CUDA driver on the system to install the [compatible](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) CUDA packages.
However, sometimes, you may want to install CUDA packages into a machine that doesn't install NVIDIA drivers (for example, the login node of a HPC cluster).
In this case, you must manually set the environment variable `CONDA_OVERRIDE_CUDA` to tell conda which packages are compatible.

For example, you want to use the installed CUDA packages on another machine where NVIDIA drivers have been installed. Run `nvidia-smi` on that machine, 
```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 545.29.06              Driver Version: 545.29.06    CUDA Version: 12.3     |
|-----------------------------------------+----------------------+----------------------+
```
the output shows the CUDA version is `12.3`.
Then, on the machine for performing installation, you may set the environment variable `export CONDA_OVERRIDE_CUDA=12.3` before running `conda install`.

## How to install conda/pip packages without the Internet access?

To install conda/pip packages without the Internet access, you need to have a machine that can connect to the Internet, and use `conda` or `pip` to install all packages in an environment.
Then, install [conda-pack](https://conda.github.io/conda-pack/):

```sh
conda install conda-pack
```

Next, running `conda pack` to pack an environment, saying `my_env`:

```sh
conda pack -n my_env -o my_env.tar.gz
```

Transfer `my_env.tar.gz` to the machine that doesn't have the Internet access.
On that machine, you can unpack the environment:
```sh
mkdir -p my_env
tar -xzf my_env.tar.gz -C my_env
source my_env/bin/activate
conda-unpack
```

## How to speed up conda/pip in China?

When you are in China, we suggest adding [Tsinghua University tuna mirrors](https://mirrors.tuna.tsinghua.edu.cn/) to your conda/pip configs to speed up downloading conda/pip packages.

In order to set up [Anaconda mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/), append the following lines to the `$HOME/.condarc` file (if it doesn't exist, you can create one):

```yaml
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

In order to set up [PyPI mirrors](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/), run

```sh
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
