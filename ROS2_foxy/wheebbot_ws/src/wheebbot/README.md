# Package directory structure (the files might not be updated, but the package structure remains valid):
```
📦wheebbot
 ┣ 📂config
 ┃ ┣ 📜IMU.yaml
 ┃ ┣ 📜ODrive.yaml
 ┃ ┣ 📜controller.yaml
 ┃ ┗ 📜urdf_params.yaml
 ┣ 📂description
 ┃ ┣ 📂meshes
 ┃ ┃ ┣ 📜full_no_knee_no_wheels.dae
 ┃ ┃ ┣ 📜full_no_knee_no_wheels.log
 ┃ ┃ ┣ 📜full_no_knee_no_wheels.mtl
 ┃ ┃ ┣ 📜full_no_knee_no_wheels.obj
 ┃ ┃ ┣ 📜wheel_black.dae
 ┃ ┃ ┣ 📜wheel_full.dae
 ┃ ┃ ┣ 📜wheel_full.log
 ┃ ┃ ┣ 📜wheel_full.mtl
 ┃ ┃ ┣ 📜wheel_full.obj
 ┃ ┃ ┗ 📜wheel_yellow.dae
 ┃ ┣ 📂sdf
 ┃ ┃ ┣ 📂WheeBBot_sdf
 ┃ ┃ ┃ ┣ 📂meshes
 ┃ ┃ ┃ ┃ ┣ 📜full_no_knee_no_wheels.dae
 ┃ ┃ ┃ ┃ ┣ 📜wheel_black.dae
 ┃ ┃ ┃ ┃ ┗ 📜wheel_yellow.dae
 ┃ ┃ ┃ ┣ 📜README.md
 ┃ ┃ ┃ ┣ 📜generate_sdf_from_erb.sh
 ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┣ 📜model.sdf
 ┃ ┃ ┃ ┗ 📜model.sdf.erb
 ┃ ┃ ┣ 📂my_camera
 ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┣ 📂my_custom_ground_plane
 ┃ ┃ ┃ ┣ 📂materials
 ┃ ┃ ┃ ┃ ┣ 📂scripts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_texture.material
 ┃ ┃ ┃ ┃ ┗ 📂textures
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asphalt.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dark_pavement.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜granite.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜granite_dark.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜obliquo_parquet.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-daria-shevtsova-1884303.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-henry-&-co-2341290.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-markus-spiske-2004166.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-pixabay-326311.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood-planks-texture-background-parquet-flooring.zip
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood_clear.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood_dark.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood_light.jpg
 ┃ ┃ ┃ ┃ ┃ ┗ 📜wood_light.png
 ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┣ 📂my_custom_ground_plane_ign
 ┃ ┃ ┃ ┣ 📂materials
 ┃ ┃ ┃ ┃ ┣ 📂scripts
 ┃ ┃ ┃ ┃ ┃ ┗ 📜test_texture.material
 ┃ ┃ ┃ ┃ ┗ 📂textures
 ┃ ┃ ┃ ┃ ┃ ┣ 📜asphalt.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜dark_pavement.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜granite.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜granite_dark.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜obliquo_parquet.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-daria-shevtsova-1884303.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-henry-&-co-2341290.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-markus-spiske-2004166.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜pexels-pixabay-326311.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood-planks-texture-background-parquet-flooring.zip
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood_clear.jpg
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood_dark.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜wood_light.jpg
 ┃ ┃ ┃ ┃ ┃ ┗ 📜wood_light.png
 ┃ ┃ ┃ ┣ 📜model.config
 ┃ ┃ ┃ ┗ 📜model.sdf
 ┃ ┃ ┗ 📜database.config
 ┃ ┣ 📂srdf
 ┃ ┗ 📂urdf
 ┃ ┃ ┣ 📜generate_urdf_from_xacro_gazebo.sh
 ┃ ┃ ┣ 📜macros.urdf.xacro
 ┃ ┃ ┣ 📜materials.urdf.xacro
 ┃ ┃ ┣ 📜parameters.urdf.xacro
 ┃ ┃ ┣ 📜wheebbot.gazebo.xacro
 ┃ ┃ ┣ 📜wheebbot.ign.xacro
 ┃ ┃ ┣ 📜wheebbot.urdf.xacro
 ┃ ┃ ┗ 📜wheebbot_ign.urdf.xacro
 ┣ 📂include
 ┣ 📂launch
 ┃ ┣ 📜display_and_test_on_RViz.launch.py
 ┃ ┣ 📜gazebo_standalone.launch.py
 ┃ ┣ 📜gazebo_wheebbot.launch.py
 ┃ ┣ 📜gzclient.launch.py
 ┃ ┣ 📜gzserver.launch.py
 ┃ ┣ 📜ign_gazebo_standalone.launch.py
 ┃ ┣ 📜ign_gazebo_wheebbot.launch.py
 ┃ ┣ 📜rviz_standalone.launch.py
 ┃ ┣ 📜rviz_standalone_ign.launch.py
 ┃ ┣ 📜spawn_entity.launch.py
 ┃ ┗ 📜spawn_entity_ign.launch.py
 ┣ 📂media
 ┃ ┣ 📂sim_graphs
 ┃ ┗ 📂videos
 ┃ ┃ ┣ 📂generated_videos
 ┃ ┃ ┣ 📂video_frames
 ┃ ┃ ┣ 📜delete_and_create_frames_folder.sh
 ┃ ┃ ┗ 📜generate_video_from_frames.sh
 ┣ 📂plugins
 ┃ ┣ 📂gazebo_classic
 ┃ ┣ 📂ign_gazebo
 ┃ ┗ 📂ros
 ┣ 📂rviz
 ┃ ┗ 📜wheebbot.rviz
 ┣ 📂src
 ┃ ┣ 📜IMU_state_publisher.py
 ┃ ┣ 📜axis_state_publisher.py
 ┃ ┣ 📜odrive_axis_config.py
 ┃ ┗ 📜odrive_axis_test.py
 ┣ 📂worlds
 ┃ ┣ 📜wheebbot.world
 ┃ ┗ 📜wheebbot_ign.world
 ┣ 📜CMakeLists.txt
 ┣ 📜model.config
 ┗ 📜package.xml
```
