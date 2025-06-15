import logging
import os
from datetime import datetime

class Logger:
    """日志工具类"""
    
    def __init__(self):
        # 创建日志目录
        self.log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        
        # 设置日志文件名
        self.log_file = os.path.join(self.log_dir, f"test_{datetime.now().strftime('%Y%m%d')}.log")
        
        # 创建logger对象
        self.logger = logging.getLogger("test")
        
        # 防止日志重复记录
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            
            # 创建文件处理器
            file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            
            # 创建控制台处理器
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            
            # 设置日志格式
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            # 添加处理器
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
    
    def debug(self, message):
        """记录调试信息"""
        self.logger.debug(message)
    
    def info(self, message):
        """记录一般信息"""
        self.logger.info(message)
    
    def warning(self, message):
        """记录警告信息"""
        self.logger.warning(message)
    
    def error(self, message):
        """记录错误信息"""
        self.logger.error(message)
    
    def critical(self, message):
        """记录严重错误信息"""
        self.logger.critical(message)

# 创建全局logger实例
logger = Logger()