import sys


def error_msg_detail(error, error_detail: sys):
    _, _, exec_tb = error_detail.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    line_number = exec_tb.tb_lineno
    msg = str(error)
    return f"Error occured in python script name {file_name} at line number {line_number} error message {msg}"


class AppException(Exception):
    def __init__(self, error_message, error_detail: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_msg_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
