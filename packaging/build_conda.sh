#!/bin/bash
set -ex
export CU_VERSION="cpu"
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
. "$script_dir/pkg_helpers.bash"

export BUILD_TYPE="conda"
setup_env 0.10.0
export SOURCE_ROOT_DIR="$PWD"
setup_conda_pytorch_constraint
setup_conda_cudatoolkit_constraint
setup_visual_studio_constraint

# need to change somethings
export CONDA_EXTRA_BUILD_CONSTRAINT="- openblas"
export CONDA_PYTORCH_CONSTRAINT="- pytorch==1.10.0"
export CONDA_PYTORCH_BUILD_CONSTRAINT="- pytorch==1.10.0"
export BUILD_VERSION="0.10.0"
# nvidia channel included for cudatoolkit >= 11
# add conda-forge and fastchan
conda build -c conda-forge -c fastchan -c defaults --no-anaconda-upload --python "$PYTHON_VERSION" packaging/torchaudio
