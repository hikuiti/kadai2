# kadai2
ロボットシステム学の講義で製作したROSを用いたpythonのプログラムです。

# 内容
このプログラムは、ロボットシステム学第10回にて製作したプログラムをもとに改良を加えた物です。

プログラムを実行すると、起動してからどれだけ経ったかをそれぞれコンマ、秒数、分で見ることができます。

# 必要な物
Raspberry Pi 4 Model B 

os;Ubuntu 18.04 LTS

ROS環境

ROS Merodic

ROS Distribution:Melodic Morenia

# 前準備
$ cd ~/catkin_ws

$ catkin_make

# 実行
端末1にて実行

$ roscore

端末2にて実行

$ rosrun mypkg comma.py

端末3にて実行

$ rosrun mypkg second.py

端末4にて実行

$ rosrun mypkg clock.py

その後、

$ rostopic echo comma.py

$ rostopic echo second.py

$ rostopic echo clock.py

にて、commaは一秒未満、secondは秒、clockは分を見ることができます。

# 動画
https://youtu.be/7IuY36KDmbM

yoububeに動画を上げてあります。

# ライセンス
[BSD 3-Clause "New" or "Revised" License]https://github.com/hikuiti/kadai2/blob/main/LICENSE
