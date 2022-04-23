-------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/80394968/164893651-97509a6f-be9f-4444-a7d0-cebec382c125.png)
-------------------------------------------------------------------------------------
# Research_Track2
*Develop third assignment of Research Track1 to control robot behavior.*
### For more information about code documentaion [click here](https://mohammadrezahajihosseini.github.io/Research_Track2/)
#
Jupyter NoteBook
================================
### What we will see in this notebook:
 * Advantages of the jupyter
 * Several widgets implemented 
 * Result after widget used

-------------------------------------------------------------------------------------
Advantages of the jupyter
----------------------
### Jupyter notebooks have three particularly strong benefits:
* They’re great for showcasing your work. You can see both the code and the results. The notebooks at [Kaggle](https://www.kaggle.com/code) is a particularly great example of this.
It’s easy to use other people’s work as a starting point. You can run cell by cell to better get an understanding of what the code does.
* Very easy to host server side, which is useful for security purposes. A lot of data is sensitive and should be protected, and one of the steps toward that is no data is stored on local machines. A server-side Jupyter Notebook setup gives you that for free.
* When prototyping, the cell-based approach of Jupyter notebooks is great. But you quickly end up programming several steps; instead of looking at object-oriented programming.

More information about jupyter notbook and how to install it on your system then refer to this [link](https://2021.aulaweb.unige.it/pluginfile.php/407745/mod_resource/content/0/rtII_2_2022.pdf)

-------------------------------------------------------------------------------------
Several widgets implemented 
----------------------
  -  RadioButtons
  -  Button & ToggleButton
  -  Matplotlib widget 
 
Has also been used *jr.publish('/movebase_client_goal', String)* and *jr.publish('/cmd_vel', Twist)*, subscribing to a ROS topic for insert coordinate by user and controll velocity

*more details [click here](https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Widget%20List.ipynb)*

-------------------------------------------------------------------------------------
Result after widget used 
----------------------
> First step 
 
   you need to launch to open simulation: 
  
    roslaunch final_assignment simulation_gmapping.launch
    roslaunch final_assignment move_base.launch
    roslaunch final_assignment master.launch
        
> Second step
 
   you need to run also jupyter notbook on your sys:
  
      jupyter-notebook
    
> Third step

   find notebook with name *jupyter_notebook_v1.ipynb*, now you have to see a page like this: 
    
![startup](https://user-images.githubusercontent.com/80394968/164909401-bbb2b87d-76b8-42fd-b498-b7db1d6579ca.jpg)
-------------------------------------------------------------------------------------
*You have to run every cell*
  - After run on cell Robot behavior:
    - you can choose from available options

![image](https://user-images.githubusercontent.com/80394968/164909532-867c45dc-f1bb-42ba-bd93-82cd6c8831b2.png)
-------------------------------------------------------------------------------------
- After run on cell Insert Goal:
  - you can insert coordinate as indicated

![Goal](https://user-images.githubusercontent.com/80394968/164909799-a3ebd9b0-699a-490c-965f-49a032de3df6.jpg)
-------------------------------------------------------------------------------------
- After run on cell Stop Button:
  - you can stop robot

![stop](https://user-images.githubusercontent.com/80394968/164909960-4b9b20f6-16b5-4310-a900-d2062907751a.jpg)
-------------------------------------------------------------------------------------
- After run on cell Driving with Keyboards:
  - you can drive robots with the following keys

![Keyboard](https://user-images.githubusercontent.com/80394968/164910028-a2ff29c9-ad6b-429d-8681-5df5f003ff2b.jpg)
-------------------------------------------------------------------------------------
- After run on cell Controll Velocity:
  - you can change angular and linear velocity of robot in three different directions and also you can creat Rate with desired frequency to continuously publish selected speed otherwise entered speed is only published once as a stroke to robot

![Velocity](https://user-images.githubusercontent.com/80394968/164910208-442ac60b-f557-41e1-894f-cd3740131ba5.jpg)
-------------------------------------------------------------------------------------
- After run on cell 3D Viewer:
  - you can see robot in 3D environment, like [RViz](http://wiki.ros.org/rviz).

![3D](https://user-images.githubusercontent.com/80394968/164910302-3cc25a9e-775a-4bc1-94f4-0c0c5ab5ccac.jpg)







