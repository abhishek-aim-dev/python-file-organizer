import os
import shutil

#for current working directory
cwd = os.getcwd()

#file mapping
file_mapping = {
    'Documents': ['.doc', '.docx', '.pdf', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': [ '.js', '.sh', '.bat'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx'],
    'Applications': ['.exe', '.app', '.msi'],
    
    
}

#create folders if they don't exist
for folder in file_mapping.keys():
    folder_path = os.path.join(cwd, folder) #folder_path to create folder in current working directory
    if not os.path.exists(folder_path): #os.path.exists() checks if the folder already exists
        os.makedirs(folder_path) #os.makedirs() creates the folder if it doesn't exist

#organize files
for file in os.listdir(cwd): #os.listdir() lists all files and folders in the current working directory
    file_path = os.path.join(cwd, file) #file_path to get the full path of the file
    if os.path.isfile(file_path): #os.path.isfile() checks if the path is a file
        file_ext = os.path.splitext(file)[1].lower() #os.path.splitext() splits the file name and extension, [1] gets the extension, .lower() converts it to lowercase
        for folder, extensions in file_mapping.items(): #iterating through the file_mapping dictionary
            if file_ext in extensions: #checking if the file extension is in the list of extensions for the folder
                shutil.move(file_path, os.path.join(cwd, folder)) #shutil.move() moves the file to the corresponding folder
                break #breaks the loop once the file is moved   

print("Files organized successfully!")


        