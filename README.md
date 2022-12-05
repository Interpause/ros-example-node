# ros-example-node

> Example module for ros2-workspace-template.

## Create a `git` Submodule

1. Create a repository on Github intialized with only a README.
2. Add the repository to the ROS workspace using:

```sh
# Substitute the below values as suitable.
git submodule add https://github.com/user/repo.git example_module
```

## Create a ROS Package

The command used to create `example_pkg` was:

```sh
cd example_module
ros2 pkg create --description "Simple pub-sub." --license MIT --build-type ament_python --maintainer-name "John-Henry Lim" example_pkg
```

While `--maintainer-email` is detected via `git`, `--maintainer-name` uses the container's username which is wrong. Hence, `--maintainer-name` is explicitly specified.

Full help:

```txt
usage: ros2 pkg create [-h] [--package-format {2,3}]
                       [--description DESCRIPTION] [--license LICENSE]
                       [--destination-directory DESTINATION_DIRECTORY]
                       [--build-type {cmake,ament_cmake,ament_python}]
                       [--dependencies DEPENDENCIES [DEPENDENCIES ...]]
                       [--maintainer-email MAINTAINER_EMAIL]
                       [--maintainer-name MAINTAINER_NAME]
                       [--node-name NODE_NAME] [--library-name LIBRARY_NAME]
                       package_name

Create a new ROS 2 package

positional arguments:
  package_name          The package name

options:
  -h, --help            show this help message and exit
  --package-format {2,3}, --package_format {2,3}
                        The package.xml format.
  --description DESCRIPTION
                        The description given in the package.xml
  --license LICENSE     The license attached to this package; this can be an
                        arbitrary string, but a LICENSE file will only be
                        generated if it is one of the supported licenses (pass
                        '?' to get a list)
  --destination-directory DESTINATION_DIRECTORY
                        Directory where to create the package directory
  --build-type {cmake,ament_cmake,ament_python}
                        The build type to process the package with
  --dependencies DEPENDENCIES [DEPENDENCIES ...]
                        list of dependencies
  --maintainer-email MAINTAINER_EMAIL
                        email address of the maintainer of this package
  --maintainer-name MAINTAINER_NAME
                        name of the maintainer of this package
  --node-name NODE_NAME
                        name of the empty executable
  --library-name LIBRARY_NAME
                        name of the empty library
```

## `requirements.txt` Escape Hatch

Some dependencies may be unavailable from the `rosdep` package manager (check [ROS Index](https://index.ros.org)). For Python dependencies, they should be added to a [`requirements.txt`](./example_pkg/requirements.txt) created within the ROS package. The ROS package's [`requirements.txt`](./example_pkg/requirements.txt) should then be composed into the workspace's [`requirements.txt`](https://github.com/Interpause/ros2-workspace-template/blob/main/requirements.txt).

## Remove a `git` Submodule

```sh
# Substitute the below values as suitable.
git rm example_module
```
