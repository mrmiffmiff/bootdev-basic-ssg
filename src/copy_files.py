import os, shutil

def copy_files(src: str, dst: str):
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
    source_directory = os.path.join(root, src)
    print("Source path may be " + source_directory)
    if not os.path.exists(source_directory):
        raise FileNotFoundError("Source path doesn't exist")
    if os.path.isfile(source_directory):
        raise NotADirectoryError("Source path points to a file")
    destination_directory = os.path.join(root, dst)
    print("Destination path may be " + destination_directory)
    if os.path.exists(destination_directory):
        if os.path.isfile(destination_directory):
            raise NotADirectoryError("Existing destination path is a file")
        print("Removing existing directory: " + destination_directory)
        shutil.rmtree(destination_directory)
    print("Creating new directory: " + destination_directory)
    os.mkdir(destination_directory)
    source_contents = os.listdir(source_directory)
    for path in source_contents:
        full_src_path = os.path.join(source_directory, path)
        if os.path.isfile(full_src_path):
            print("Copying file " + full_src_path + " into folder " + destination_directory)
            shutil.copy(full_src_path, destination_directory) # Should use base file name and copy into that directory
        else:
            new_rel_source = os.path.relpath(full_src_path, root)
            full_dst_path = os.path.join(destination_directory, path)
            new_rel_dst = os.path.relpath(full_dst_path, root)
            print("Initiating recursive copying of files from " + full_src_path + " to " + full_dst_path)
            copy_files(new_rel_source, new_rel_dst)