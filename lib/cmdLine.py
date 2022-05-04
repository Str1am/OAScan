import argparse
def get_options():
    parser = argparse.ArgumentParser(usage='python3 OAScan.py -u https://www.baidu.com')
    target = parser.add_argument_group("Target", "Those options can be used to load targets")
    target.add_argument("-u", metavar='TARGET', dest="target_single", type=str, default="",
                        help="scan a single target (e.g. https://www.baidu.com)")

    target.add_argument("-f", metavar='TARGET', dest="target_file", type=str, default="",
                        help="scan target in file")

    target.add_argument("-m", metavar='module', dest="target_module", type=str, default="",
                        help="provide a module eg:Seeyon Tongda Fanwei")

    args = parser.parse_args()
    return args

    # #单个目标
    # target_single_list = []
    # if args.target_single:
    #     msg = '[+] Load target : {}'.format(args.target_single)
    #     target_single_list.append(args.target_single)
    #     return target_single_list
    #
    # #一个文件
    # target_file_list = []
    # if args.target_file:
    #     with open(args.target_file, 'r', encoding='utf8') as f:
    #         targets = f.readlines()
    #         for target in targets:
    #             target_file_list.append(target.strip('\n'))
    #     return target_file_list

    # #指定一个module
    # if args.target_module:
    #     return args.target_module