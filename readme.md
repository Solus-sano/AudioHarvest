# AudioHarvest

## 简介

本项目使用bilibili提供的API下载b站视频中的音频文件到指定文件夹

## 使用方法

1.修改config.py中的参数
- source_file 参数为csv文件，其中第一列为歌名，第二列为对应的b站音源url，第三列为对应音源在url中的p数
- cache_dir 参数为音频文件存储的文件夹路径
2.运行refresh.py, 脚本会根据csv提供的信息更新cache_dir中的音频文件

