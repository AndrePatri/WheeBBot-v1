# To build the ws with colcon:

- colcon build --> builds all the packages
- colcon build --packages-select package_name --> builds only the selected packages
- colcon build --allow-overriding wheebbot --> to override a previous build
- add the --symlink-install option so that you can modify and re-run a script without having to re-compile. Remember to make it executable with chmod +x
