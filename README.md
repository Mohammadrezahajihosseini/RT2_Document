# Research_Track2

*Develop third assignment of Research Track1 to control robot behavior.*
### For more information [click here](https://mohammadrezahajihosseini.github.io/Research_Track2/)
-------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/80394968/164893651-97509a6f-be9f-4444-a7d0-cebec382c125.png)

Jupyter NoteBook
================================
### What we will see in this notebook:
 * Advantages of the jupyter
 * Several widgets implemented 
 * How it works 
 * Result after widget used
-------------------------------------------------------------------------------------
Advantages of the jupyter
----------------------
### *Jupyter notebooks have three particularly strong benefits:
* They’re great for showcasing your work. You can see both the code and the results. The notebooks at [Kaggle](https://www.kaggle.com/code)is a particularly great example of this.
It’s easy to use other people’s work as a starting point. You can run cell by cell to better get an understanding of what the code does.
* Very easy to host server side, which is useful for security purposes. A lot of data is sensitive and should be protected, and one of the steps toward that is no data is stored on local machines. A server-side Jupyter Notebook setup gives you that for free.
* When prototyping, the cell-based approach of Jupyter notebooks is great. But you quickly end up programming several steps;instead of looking at object-oriented programming.


Once it was ready all the following cases you can download or fork, the repository in your workspace. At this stage to start the simulation you have to do:

1. Use: 
```
 $catkin_make
```
To compile the new packages installed on workspace, remember to use catkin_make in the workspace root file

2. Start two launch files:
```
$roslaunch final_assignment simulation_gmapping.launch
$roslaunch final_assignment move_base.launch
```
Practically with the first launch file you start the Gazebo and rviz simulator and you can see robots within the Gazebo and with second launch file you use to know the map and obstacles that is used to send goal to the robot.

Now then visualize this map in your system:
![photo_2022-01-26_11-50-54](https://user-images.githubusercontent.com/80394968/151150507-fb636911-7eff-4a1c-8d6b-32914645cd42.jpg)

It can happen to run the following launch files many times and finding an error on the operating system part (in my case linux) log file disk is full, because the directory that contains the cache file has a limited size so it can cause this. You can solve the following problem by doing:
```
$rosclean purge
```
Clears all cache files created by the system. Be careful in some cases it can also delete the cache important files so used only in case of need.

3. To make run master node you need to launch:
```
$roslaunch final_assignment master.py
```
After launching the master node you see three new shell consoles open which are to control robot behavior, one of them the master console which allows you to go to different layer of robots, there are three levels which you can control via master console:

1. Coordinates entered by the user 
2. Driving robots with keyboards
3. Drive robots through user, avoid going against obstacles

Remember for this part a konsole opens in the system to guide the robot. If you have not installed konsole package you may have errors on execution of the program. To install it you can do: 
```
$sudo apt-get update
$sudo apt-get install konsole
```


