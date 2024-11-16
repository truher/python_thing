# python_thing

How to make a python thing using github actions.

The goal is to build a "nightly" or "on push" package that is publicly
available using pip.

Eventually the idea is to build the Raspberry Pi package containing GTSAM,
which means building it for ARM using a Github Action

## notes

see https://packaging.python.org/en/latest/tutorials/packaging-projects/

python3 -m pip install --upgrade build

Pypi itself is not a good host for this.

https://discuss.python.org/t/publishing-nightly-builds-on-test-pypi-org-with-a-time-based-retention-policy/3152

"PyPI/warehouse is not really designed for large, transient artifacts"

Olivier seems to have chosen Anaconda for Scipy.

I think it's possible to ust GitHub itself to host the "wheel", and to tell pip
where to find them.

Or maybe you're supposed to let pip build the wheel itself?

Can Github build for ARM?

https://github.com/orgs/community/discussions/25650

Seems like maybe?

https://github.com/pguyot/arm-runner-action

Here's an example that retains the built artifacts

https://github.com/nabaztag2018/pynab/blob/master/.github/workflows/arm-runner.yml

