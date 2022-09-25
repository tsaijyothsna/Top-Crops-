import os
import shutil
#commodity1 = onion
#commodity2 = potato
#commodity3 = Cabbage
def Rename():
    ###############################################path###########################################
    path = os.getcwd() + os.path.sep + "Database"
    path1 = os.getcwd() + os.path.sep + "Temp_DataBase"
    os.mkdir(path1)
    #########################################Apple################################################
    old_file_name = path + os.path.sep + "commodity1" +os.path.sep + "Agmarknet_Price_Report.xls"
    new_file_name = path + os.path.sep + "commodity1" +os.path.sep + "apple.xls"
    destination = path1 + os.path.sep + 'apple.xls'
    os.rename(old_file_name, new_file_name)
    shutil.copyfile(new_file_name, destination)
    #########################################Banana##################################################
    old_file_name1 = path + os.path.sep + "commodity2" + os.path.sep + "Agmarknet_Price_Report.xls"
    new_file_name1 = path + os.path.sep + "commodity2" + os.path.sep + "banana.xls"
    destination1 =  path1 + os.path.sep + 'banana.xls'
    os.rename(old_file_name1, new_file_name1)
    shutil.copyfile(new_file_name1, destination1)
    ########################################Onion#######################################################
    old_file_name2 = path + os.path.sep + "commodity3" + os.path.sep + "Agmarknet_Price_Report.xls"
    new_file_name2 = path + os.path.sep + "commodity3" + os.path.sep + "onion.xls"
    destination2 = path1 + os.path.sep + 'onion.xls'
    os.rename(old_file_name2, new_file_name2)
    shutil.copyfile(new_file_name2, destination2)
    #######################################Potato#######################################################
    old_file_name3 = path + os.path.sep + "commodity4" + os.path.sep + "Agmarknet_Price_Report.xls"
    new_file_name3 = path + os.path.sep + "commodity4" + os.path.sep + "potato.xls"
    destination3 = path1 + os.path.sep + 'potato.xls'
    os.rename(old_file_name3, new_file_name3)
    shutil.copyfile(new_file_name3, destination3)
    ####################################cabbage##########################################################
    old_file_name4 = path + os.path.sep + "commodity5" + os.path.sep + "Agmarknet_Price_Report.xls"
    new_file_name4 = path + os.path.sep + "commodity5" + os.path.sep + "cabbage.xls"
    destination4 = path1 + os.path.sep + 'cabbage.xls'
    os.rename(old_file_name4, new_file_name4)
    shutil.copyfile(new_file_name4, destination4)
    Y = "Report Name is Changed to Generic Name"
    ##########################################end##########################################################
    return(Y)
