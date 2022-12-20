# 通过codeVis生成了不同channel的文件后，调用这个文件来把所有channel的instances合并到一个总的instances中，形成数据增强

import os

# 建立txt文件夹下的文件，放路径，放标签
root_path_csvs = 'csvs/'
root_path_img = 'img/'
channel_paths = ['/bgr_img/', '/rbg_img/', '/rgb_img/', '/brg_img/', '/gbr_img/', '/grb_img/']

for csv_file in os.listdir(root_path_csvs):
    # 从camel-1.2.csv中取出项目名
    project_name = os.path.splitext(csv_file)[0]
    print(project_name + " begin!")

    # 获取目标文件夹的路径
    save_file_path = root_path_img + project_name + '/instances.txt'
    # 打开文件，如果没有则创建
    save_file = open(save_file_path, 'w')

    # 合并所有channel里的instance.txt到一个instance.txt中，用来做数据增强
    for channel_path in channel_paths:
        channel_instance_file_path = root_path_img + project_name + channel_path + 'instances.txt'

        # 遍历单个文件，读取行数
        for line in open(channel_instance_file_path):
            save_file.writelines(line)

    # 关闭文件
    save_file.close()

    print(project_name + " done!")