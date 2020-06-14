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



import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")

# 添加了元素就会报错
args = parser.parse_args()