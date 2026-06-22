class CourseNotFoundException(Exception):
    def __init__(self, message: str = "课程不存在"):
        self.message = message
        super().__init__(message)


class CoursePermissionException(Exception):
    def __init__(self, message: str = "无权操作该课程"):
        self.message = message
        super().__init__(message)


class CourseStatusTransitionException(Exception):
    def __init__(self, message: str = "课程状态流转不合法"):
        self.message = message
        super().__init__(message)
