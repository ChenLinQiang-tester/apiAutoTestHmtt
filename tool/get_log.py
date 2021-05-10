import logging.handlers
import os
from config import base_path


class GetLog:
    # 新建日志器变量
    __logger = None
    # 新建获取日志器方法

    @classmethod
    def get_logger(cls):
        # 判断日志器为空：
        if cls.__logger is None:
            # 获取日志器
            cls.__logger = logging.getLogger()
            # 设置日志等级
            cls.__logger.setLevel(logging.INFO)
            # 获取日志处理器对象
            # sh = logging.StreamHandler()
            th = logging.FileHandler(filename=os.path.join(base_path, "log", "api.log"), encoding="utf-8")
            # 设置处理器获取日志级别

            # 添加格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s (%(funcName)s：%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器对象中
            th.setFormatter(fm)
            # 添加处理器添加到日志器中
            cls.__logger.addHandler(th)
        # 返回日志器
        return cls.__logger


if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("测试：info\n")
    log.warning("测试：warning")
    log.error("测试：error")
