from lib.cmdLine import get_options
args = get_options()
def get_target(args):
    #单个目标
    target_single_list = []
    if args.target_single:
        msg = '[+] Load target : {}'.format(args.target_single)
        target_single_list.append(args.target_single)
        return target_single_list

    #一个文件
    target_file_list = []
    if args.target_file:
        with open(args.target_file, 'r', encoding='utf8') as f:
            targets = f.readlines()
            for target in targets:
                target_file_list.append(target.strip('\n'))
        return target_file_list

def get_single_module(args):
    #指定一个module
    if args.target_module:
        return args.target_module
