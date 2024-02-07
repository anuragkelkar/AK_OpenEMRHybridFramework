import os

current_dir = os.getcwd()
main_project_dir = current_dir.split("HybridFramework")[0]
main_project_dir = main_project_dir + "HybridFramework\\HybridFramework"
test_data_path = main_project_dir+"\\test_data"

print(test_data_path)