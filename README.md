![image](https://user-images.githubusercontent.com/80394968/164916675-09dad27d-4283-4517-8c35-3d83bc5d5b1b.png)            

**Author:** *Mohammad Reza Haji Hosseini*

**matricola:** *4394567* 

**Project supervisor:** *Carmine Recchiuto*

**Year:** *2021-22* 
# Research_Track2
*Develop third assignment of Research Track1 to control robot behavior in three modality.*

[Documentaion Link here](https://mohammadrezahajihosseini.github.io/Research_Track2/)
-------------------------------------------------------------------------------------

Launch program
================================
- First level you need to have ROS noetic version installed on your system, for how to install check [here](http://wiki.ros.org/noetic/Installation)

- Second level you need to creat your own repository, to do that you need to proceed in this way:
  ```
  $ mkdir -p catkin_ws/src
  $ cd catkin_ws/src
  ```
- Frok package from my repository 
  ```
  $ git clone https://github.com/Mohammadrezahajihosseini/Research_Track2.git
  $ cd ..
  $ catkin_make
  ```
- Now you can launch first lanunch file, which allows you to see simulator [Gazebo](https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=connect_ros) and [Rviz](http://wiki.ros.org/rviz)
  ```
  $ source devel/setup.bash
  $ roslaunch final_assignment simulation_gmapping.launch
  ```
 - you need also to launch anthore launch file with name [*move_base*](http://wiki.ros.org/move_base), which allows to provides an implementation of an action. 

   ```
   $ source devel/setup.bash
   $ roslaunch final_assignment move_base.launch
   ```
 - Remember that to launch master launch file, it is necessary to install konsole
   ```
   $ sudo apt-get update
   $ sudo apt install konsole
   ```
 - Now then visualize this map in your system:
![photo_2022-01-26_11-50-54](https://user-images.githubusercontent.com/80394968/151150507-fb636911-7eff-4a1c-8d6b-32914645cd42.jpg)

- It can happen to run the following launch files many times and finding an error on the operating system part (in my case linux) log file disk is full, because the directory that contains the cache file has a limited size so it can cause this. You can solve the following problem by doing:
  ```
  $ rosclean purge
  ```

- Now you can launch master launch file:
  ```
  $ source devel/setup.bash
  $ roslaunch final_assignment master.py
  ```
After launching the master node you see three new shell consoles open which are to control robot behavior, one of them the master console which allows you to go to different layer of robots, there are three levels which you can control via master console:

*1. Use the coordinates entered by the user*

*2. Driving robots with keyboards*

*3. Drive robots through user, avoid going against obstacles*




