import os 
from pathlib import Path


directory = {
    'IMAGES': ['.jpg','.jpeg','.png','.jfif','.webp','.svg','.gif','.bmp','.ico','.tiff','.tif'],
    'MOVIES':   ['.mov','.mp4','.m4a'],
    'DOCUMENTS':['.doc','.docx','.pdf','.rtf','.txt','.md'],
    'AUDIO':['.mp3','.wav'],
    'INSTALLER':['.exe','.apk','.jar','.msi'],
    'CODE':['.py','.java','.c','.cs'],
    'NOTEBOOKS':['.ipynb'],
    'COMPRESSED':['.zip','.rar'],
    'CISCO' : ['.pkt'],
    'MATLAB' : ['.mlx'],
    'EXCEL':['.xlsx','.xls','.csv'],
    'POWERPOINT':['.ppt','.pptx'],
    'SUBTITLES':['.srt','.vtt']
}

def pickDirectory(value):
    for category,suffixes in directory.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'Misc'


def orgDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        folder = pickDirectory(filetype)
        directoryPath = Path(folder)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        newfilePath = directoryPath.joinpath(filePath.name)
        i = 1
        while newfilePath == filePath:
            filePath = directoryPath.joinpath(f"{filePath.stem}_{i}{filePath.suffix}")
            i += 1
        if newfilePath.exists():
            print(f"Failed to rename file {filePath.name}")
        else:
            filePath.rename(newfilePath)
        

orgDirectory()