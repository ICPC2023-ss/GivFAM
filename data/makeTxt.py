# 通过csvs里的文件，生成txt目录下的文件，生成的文件是需要转化为img的java文件

import numpy as np
import pandas as pd
import os


def extract_csv_instances(path):
    csv_instances = pd.read_csv(path)

    # 获取文件名
    instances = np.array(csv_instances['file_name'])
    instances = instances.tolist()

    # 获取标签
    labels = np.array(csv_instances['bug'])
    labels = labels.tolist()
    for index, label in enumerate(labels):
        if label > 1:
            labels[index] = 1

    return instances, labels


def parse_source(project_root_path, csv_file_instances, csv_file_labels, package_heads):
    count = 0
    existed_paths_and_labels = []
    for dir_path, dir_names, file_names in os.walk(project_root_path):

        # 如果文件夹下没有文件，直接跳过该文件夹
        if len(file_names) == 0:
            continue

        index = -1
        for _head in package_heads:
            index = int(dir_path.find(_head))
            if index >= 0:
                break
        if index < 0:
            continue

        package_name = dir_path[index:]
        package_name = package_name.replace(os.sep, '.')

        for file in file_names:
            if file.endswith('java'):
                file_name = os.path.splitext(file)[0]

                # 遍历csv文件，如果有的话，就把文件路径和标签存起来
                for index, instance in enumerate(csv_file_instances):
                    if str(package_name + "." + str(file_name)) == instance:
                        file_real_path = "../data/"+dir_path+'/'+file
                        file_real_path = file_real_path.replace('\\', '/')  # windows下路径为'\',需替换为'/'
                        existed_paths_and_labels.append([file_real_path, csv_file_labels[index]])
                        count += 1
                        break

    for csv_file_instance in csv_file_instances:
        if csv_file_instance not in existed_paths_and_labels[0]:
            print('This file is not in csv list:' + csv_file_instance)

    print("data size : " + str(count))
    return existed_paths_and_labels


# 建立txt文件夹下的文件，放路径，放标签
package_heads = ['org', 'gnu', 'bsh', 'javax', 'com', 'fr']
root_path_csvs = 'csvs/'
root_path_archives = 'archives/'
root_path_txt = 'txt/'

for csv_file in os.listdir(root_path_csvs):
    # 从camel-1.2.csv中取出项目名
    project_name = os.path.splitext(csv_file)[0]
    print(project_name + " begin!")

    # 取csv中有标签的文件
    path_csv = root_path_csvs + project_name + '.csv'
    csv_file_instances, csv_file_labels = extract_csv_instances(path_csv)

    # 取代码的文件夹
    path_archives = root_path_archives + project_name
    existed_paths_and_labels = parse_source(path_archives, csv_file_instances, csv_file_labels, package_heads)
    np.savetxt(root_path_txt+project_name+'.txt', existed_paths_and_labels, fmt="%s", delimiter=" ")

    print(project_name + " done!")