# def func(dir)->None:
#     res = []
#     for dir_path, dir_name,file_name in os.walk(dir):
#         dir_size = 0
#         for file in file_name:
#             file_path = os.path.join(dir_path, file)
#             size = os.path.getsize(file_path)
#             dir_size += size
#             res.append({'path': file_path, 'type': 'file', 'size': size, 'parent_directory': dir_path})
#         res.append(
#             {'path': dir_path, 'type': 'directory', 'size': dir_size, 'parent_directory': os.path.dirname(dir_path)})
    # print(result)



#     with (open('task2.json', "w", encoding="UTF-8") as f,
#           open('task2.pickle', 'wb') as f1,
#           open('task2.csv','w',encoding="UTF-8") as f2):
#         pickle.dump(res, f1)
#         json.dump(res, f, ensure_ascii=False, indent=2)
#         csv_write = csv.DictWriter(f2, fieldnames=['path', 'type', 'size', 'parent_directory'])
#         csv_write.writeheader()
#         csv_write.writerows(res)


# if __name__=="__main__":
#for dir_path, dir_name, file_name in os.walk('C:\Users\chupa\OneDrive\Рабочий стол\Hometsk8'):
    #    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
#     func('C:\Users\chupa\OneDrive\Рабочий стол\Hometsk8')






