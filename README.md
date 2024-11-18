# python_thing

How to make a python thing using github actions.

The goal is to build a "nightly" or "on push" package that is publicly
available using pip.

Eventually the idea is to build the Raspberry Pi package containing GTSAM,
which means building it for ARM using a Github Action

## building

see https://packaging.python.org/en/latest/tutorials/packaging-projects/

make sure the "build" tool is installed.

python3 -m pip install --upgrade build
python3 -m build

## try uploading from my desktop

first i registered at pypi.

apparently two-factor auth is required, so i did that.

made an API token.

installed twine

python3 -m pip install --upgrade twine

then do the upload

python3 -m twine upload --repository testpypi dist/*

this requires pasting the token; i guess it would be a github secret?

i made a venv and installed the thing, and it works.

```
$ python3 -m venv foo
$ cd foo/
$ source bin/activate

(foo) $ python3 -m pip install --index-url https://test.pypi.org/simple/ example-package-truher     
Looking in indexes: https://test.pypi.org/simple/
Collecting example-package-truher
  Downloading https://test-files.pythonhosted.org/packages/e4/66/7522c7f8189f5f9a295cf13bf8b63eb0c9e5f098696d0911079b616c8e8c/example_package_truher-0.0.dev20241117-py3-none-any.whl (3.4 kB)
Installing collected packages: example-package-truher
Successfully installed example-package-truher-0.0.dev20241117

(foo) $ python3
>>> import example_package_truher.example as example
>>> example.add_one(1)
2
```

It looks like lots of projects (e.g. tensorflow) use pypi for nightly dev builds

https://pypi.org/project/tb-nightly

has builds called things like 2.19.0a20241117

the naming standard

https://peps.python.org/pep-0440

says that this means the "alpha" for version 2.19.0.

other projects, e.g.

https://pypi.org/project/tf-nightly-cpu

use names like 2.19.0.dev20241117 

which means a "developmental" release.

PyPI limits projects to 10GB, so presumably we'd need to manually purge old dev
versions periodically, which seems like no big deal.

Some other projects (e.g. scipy) use the pypi service of anaconda, but i'd prefer
pypi over anaconda, just because pypi is an org and anaconda is a com.

## how to upload from github actions

The "normal" way now is apparently to use "trusted publishing" which means
"let github do it"

https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

so i went to https://test.pypi.org/manage/account/publishing/

and configured project name "example-package-truher", owner "truher", repository "python_thing"
workflow "python-publish.yml" and i left the environment name blank.

so that was the wrong thing to do since "example-package-truher" already exists.  :-)

so i went to the "publishing" tab of that project and repeated the process, which worked.

i filled out python-publish.yml to push test, we'll see if it works.


## Building for ARM

Can Github build for ARM?

https://github.com/orgs/community/discussions/25650

Seems like maybe?

https://github.com/pguyot/arm-runner-action

Here's an example that retains the built artifacts

https://github.com/nabaztag2018/pynab/blob/master/.github/workflows/arm-runner.yml

