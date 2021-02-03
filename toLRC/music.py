import time
import pygame


class Music(object):
    __total_time = 0
    __current_seconds = 0
    __status = True # 播放
    __file_path = ''
    __obj = None

    def __init__(self,file_path):
        self.__file_path = file_path
        __obj = pygame.mixer
        __obj.init()
        #加载音乐
        __obj.music.load(self.__file_path)
    
    def play(self):
        """
        播放
        """    
        # playsound(self.__file_path)
        
        __obj.music.play()


    def stop(self):
        """
        暂停
        """    
        pass


    def readM(self):
        """
        读取当前播放进度
        """    
        pass


    def readTotalTime(self):
        """
        读取mp3当前总时长
        """    
        pass

    
    
        

