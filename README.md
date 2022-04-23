-------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/80394968/164893651-97509a6f-be9f-4444-a7d0-cebec382c125.png)
-------------------------------------------------------------------------------------
# Research_Track2
*Develop third assignment of Research Track1 to control robot behavior.*
### For more information about code [click here](https://mohammadrezahajihosseini.github.io/Research_Track2/)
#
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

*more details [click here](https://github.com/jupyter-widgets/ipywidgets/blob/master/docs/source/examples/Widget%20List.ipynb)
