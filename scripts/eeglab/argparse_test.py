# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
#
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))



# import argparse

# parser = argparse.ArgumentParser()
# parser.parse_args()



# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
#
# # 添加了元素就会报错
# args = parser.parse_args()

# python3 argparse_test.py --help

# import argparse
#
# parser = argparse.ArgumentParser()
# # parser.add_argument("echo",help=" echo the string you use here!")
# parser.add_argument('square',help="input the digital number")
# args = parser.parse_args()
# print(args.square**2)


# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("echo",help=" echo the string you use here!")
# args = parser.parse_args()
# # print(args.echo)

#
# import argparse
#
# parser = argparse.ArgumentParser()
# # parser.add_argument("echo",help=" echo the string you use here!")
# parser.add_argument('square',help="input the digital number",type=int)
# args = parser.parse_args()
# print(args.square**2)

import argparse

# 创建一个解析对象
parser = argparse.ArgumentParser()
# parser.add_argument("echo",help=" echo the string you use here!")

# 向对象中添加相关命令行参数或选项,每一个add_argument方法对应一个参数或选项

parser.add_argument('square', help="input the digital number", type=int)
# 调用parse_args()方法进行解析
args = parser.parse_args()
print(args.square ** 2)



