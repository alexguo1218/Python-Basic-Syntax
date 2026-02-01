# 异常处理
# try:
#     print("# # # # # # # # # # #")
#     print(my_name)
#     print("# # # # # # # # # # #")
# except NameError as e: # 要捕获的异常类型是NameError
#     print("程序异常,异常信息:", e)


# try:
#     print("# # # # # # # # # # #")
#     # print(my_name)
#     print(1 / 0)
#     print("# # # # # # # # # # #")
# except NameError as e: # 要捕获的异常类型是NameError
#     print("程序异常,异常信息:", e)
# except ZeroDivisionError as e: # 要捕获的异常类型是ZeroDivisionError
#     print("程序异常,异常信息:", e)

# try:
#     print("# # # # # # # # # # #")
#     # print(my_name)
#     # print(1 / 0)
#     print("ABC"[10])
#     print("# # # # # # # # # # #")
# except NameError as e: # 要捕获的异常类型是NameError
#     print("程序异常,异常信息:", e)
# except ZeroDivisionError as e: # 要捕获的异常类型是ZeroDivisionError
#     print("程序异常,异常信息:", e)
# except IndexError as e: # 要捕获的异常类型是IndexError
#     print("程序异常,异常信息:", e)

try:
    print("# # # # # # # # # # #")
    # print(my_name)
    # print(1 / 0)
    # print("ABC"[10])
    print("ABC".hello)
    print("# # # # # # # # # # #")
except NameError as e: # 要捕获的异常类型是NameError
    print("程序异常,异常信息:", e)
except ZeroDivisionError as e: # 要捕获的异常类型是ZeroDivisionError
    print("程序异常,异常信息:", e)
except IndexError as e: # 要捕获的异常类型是IndexError
    print("程序异常,异常信息:", e)
except Exception as e: # 要捕获的异常类型是Exception(所有异常的基类)
    print("程序异常,异常信息:", e)
finally: # 无论是否发生异常，都会执行
    print("程序执行完毕，内存已释放~")


# 异常的传递
def func1():
    print("func1...running...")
    func2()

def func2():
    print("func2...running...")
    func3()

def func3():
    print("func3...running...")
    print(my_name)

if __name__ == "__main__":
    try:
        func1()
    except Exception as e:
        print("程序异常,异常信息:", e)
    finally:
        print("程序执行完毕，内存已释放~")
